from django.urls import path
from .views import hello_world, incidents_view, specific_incident_view

urlpatterns = [
    path('', incidents_view),
    path('<int:incident_id>', specific_incident_view)
]
