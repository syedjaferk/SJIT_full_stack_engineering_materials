from django.shortcuts import render
from django.http import JsonResponse
from .models import Incidents
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def hello_world(request):
    print("Request Object ", dir(request))
    # <- logic
    return JsonResponse({"status": "Hello World"})

@csrf_exempt
def incidents_view(request):
    if request.method == 'GET':
        incidents = Incidents.objects.all()
        response = []
        for incident in incidents:
            response.append(
                {   
                    "id": incident.id,
                    "title": incident.title,
                    "description": incident.description
                }
            )
        return JsonResponse(response, safe=False)
    elif request.method == 'POST':
        data = request.body
        data = data.decode()
        data = json.loads(data)
        new_incident = Incidents(title=data.get("title", ""),
                                description=data.get("description", ""))
        new_incident.save()
        return JsonResponse({"status": f"Incident Created {new_incident.id}"})

@csrf_exempt
def specific_incident_view(request, incident_id):
    if request.method == 'GET':
        try:
            incident = Incidents.objects.get(id=incident_id)
            return JsonResponse({"id": incident.id, "title": incident.title, "description": incident.description}, safe=False)
        except Exception as ex:
            return JsonResponse({"status": "Not Found"}, status=404)