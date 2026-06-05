from django.shortcuts import render

from .models import Student

# Create your views here.


def student_list(request):
    students = Student.objects.all()
    return render(request, "students/list.html", {"students": students})
