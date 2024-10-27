from rest_framework import generics, status
from rest_framework.response import Response
from .models import SpyCat
from .serializers import SpyCatSerializer


class SpyCatListView(generics.ListAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer


class SpyCatCreateView(generics.CreateAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer


class SpyCatRetrieveView(generics.RetrieveAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer
    lookup_field = 'id'


class SpyCatUpdateSalaryView(generics.UpdateAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        spy_cat = self.get_object()

        salary = request.data.get('salary')
        if salary is None:
            return Response({"error": "Salary field is required."}, status=status.HTTP_400_BAD_REQUEST)

        spy_cat.salary = salary
        spy_cat.save()

        serializer = self.get_serializer(spy_cat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class SpyCatDeleteView(generics.DestroyAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer
    lookup_field = 'id'
