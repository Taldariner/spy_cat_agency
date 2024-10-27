from django.db import models
from django.core.exceptions import ValidationError
from cats.models import SpyCat


class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        if self.cat:
            raise ValidationError("Cannot delete a mission that is assigned to a cat.")
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Mission (Cat: {self.cat.name if self.cat else 'Unassigned'}, Complete: {self.complete})"


class Target(models.Model):
    mission = models.ForeignKey(Mission, related_name='targets', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    notes = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.complete and self.notes:
            raise ValidationError("Cannot update notes for a completed target.")
        if self.mission.complete:
            raise ValidationError("Cannot update notes as the mission is already completed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Target {self.name} (Mission ID: {self.mission.id})"