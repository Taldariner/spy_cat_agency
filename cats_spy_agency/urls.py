from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/',    admin.site.urls),
    path('cats/',     include('cats.urls')),
    path('missions/', include('missions.urls'))
]