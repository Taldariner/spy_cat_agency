from django.urls import path
from .views import SpyCatListView, SpyCatCreateView, SpyCatRetrieveView, SpyCatUpdateSalaryView, SpyCatDeleteView


app_name = 'cats'
urlpatterns = [
    path('',                        SpyCatListView.as_view(), name='spycat-list'),
    path('create',                  SpyCatCreateView.as_view(), name='spycat-create'),
    path('<int:id>/',               SpyCatRetrieveView.as_view(), name='spycat-detail'),
    path('<int:id>/update_salary',  SpyCatUpdateSalaryView.as_view(), name='spycat-update-salary'),
    path('<int:id>/delete',         SpyCatDeleteView.as_view(), name='spycat-delete'),
]
