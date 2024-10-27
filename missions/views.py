from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .models import Mission, SpyCat
from .serializers import MissionSerializer, TargetSerializer


class MissionListView(generics.ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionCreateView(generics.CreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionDetailView(generics.RetrieveAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    lookup_field = 'id'


class MissionTargetsUpdateView(generics.UpdateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        mission = self.get_object()

        if mission.complete:
            raise ValidationError("Cannot update targets for a completed mission.")

        targets_data = request.data.get('targets', [])
        if not isinstance(targets_data, list) or len(targets_data) == 0:
            return Response({"error": "Invalid targets data."}, status=status.HTTP_400_BAD_REQUEST)

        for target_data in targets_data:
            target_id = target_data.get('id')
            if target_id is None:
                return Response({"error": "Target ID is required."}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                target = mission.targets.get(id=target_id)
            except Target.DoesNotExist:
                return Response({"error": f"Target with ID {target_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

            if target.complete:
                return Response({"error": f"Cannot update a completed target (Target ID: {target_id})."}, status=status.HTTP_400_BAD_REQUEST)

            target.notes = target_data.get('notes', target.notes)
            target.complete = target_data.get('complete', target.complete)
            target.save()

        return Response({"message": "Targets updated successfully."}, status=status.HTTP_200_OK)



class MissionDeleteView(generics.DestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    lookup_field = 'id'

    def perform_destroy(self, instance):
        if instance.cat:
            raise ValidationError("Cannot delete a mission that is assigned to a cat.")
        instance.delete()


class MissionAssignCatView(APIView):
    def post(self, request, mission_id, cat_id):
        try:
            mission = Mission.objects.get(id=mission_id)
            cat = SpyCat.objects.get(id=cat_id)
        except Mission.DoesNotExist:
            return Response({"error": "Mission not found."}, status=status.HTTP_404_NOT_FOUND)
        except SpyCat.DoesNotExist:
            return Response({"error": "Cat not found."}, status=status.HTTP_404_NOT_FOUND)

        if mission.cat:
            return Response({"error": "Mission already assigned to a cat."}, status=status.HTTP_400_BAD_REQUEST)

        mission.cat = cat
        mission.save()
        return Response({"message": "Cat assigned to mission successfully."}, status=status.HTTP_200_OK)
