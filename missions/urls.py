from django.urls import path
from .views import (
    MissionListView, MissionCreateView, MissionDetailView,
    MissionTargetsUpdateView, MissionDeleteView, MissionAssignCatView
)

app_name = 'missions'
urlpatterns = [
    path('',                                         MissionListView.as_view(), name='mission-list'),
    path('create',                                   MissionCreateView.as_view(), name='mission-create'),
    path('<int:id>',                                 MissionDetailView.as_view(), name='mission-detail'),
    path('<int:id>/update_targets',                  MissionTargetsUpdateView.as_view(), name='mission-update-targets'),
    path('<int:id>/delete',                          MissionDeleteView.as_view(), name='mission-delete'),
    path('<int:mission_id>/assign-cat/<int:cat_id>', MissionAssignCatView.as_view(), name='mission-assign-cat'),
]
