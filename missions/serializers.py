from rest_framework import serializers
from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'complete']

    def validate(self, data):
        if self.instance and self.instance.complete and 'notes' in data:
            raise serializers.ValidationError("Cannot update notes for a completed target.")
        return data


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'complete', 'targets']

    def validate_targets(self, value):
        if not (1 <= len(value) <= 3):
            raise serializers.ValidationError("A mission must have between 1 and 3 targets.")
        return value

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission

    def update(self, instance, validated_data):
        if 'complete' in validated_data and validated_data['complete']:
            instance.complete = True
            instance.save()

        targets_data = validated_data.pop('targets', None)
        if targets_data:
            for target_data in targets_data:
                target = Target.objects.get(id=target_data['id'])
                if instance.complete or target.complete:
                    raise serializers.ValidationError("Cannot update a completed target or mission.")
                target.notes = target_data.get('notes', target.notes)
                target.save()

        return instance
