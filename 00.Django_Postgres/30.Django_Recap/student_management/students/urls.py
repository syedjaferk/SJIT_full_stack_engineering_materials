from django.urls import path

from .views import add_student, delete_student, student_list, update_student

urlpatterns = [
    path("", student_list, name="student_list_view"),
    path("add/", add_student, name="student_add_view"),
    path("update/<int:pk>/", update_student, name="student_update_view"),
    path("delete/<int:pk>/", delete_student, name="student_delete_view"),
]
