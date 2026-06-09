from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Student

# Create your views here.


def student_list(request):
    students = Student.objects.all()
    return render(request, "students/list.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            # Creating an Object
            Student.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                age=form.cleaned_data["age"],
            )
            return redirect("student_list_view")
    else:
        form = StudentForm()

    return render(request, "students/add.html", {"form": form})


def update_student(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student.name = form.cleaned_data["name"]
            student.email = form.cleaned_data["email"]
            student.age = form.cleaned_data["age"]

            student.save()
            return redirect("student_list_view")
    else:
        form = StudentForm(
            initial={"name": student.name, "email": student.email, "age": student.age}
        )

    return render(request, "students/add.html", {"form": form})


def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect("student_list_view")
