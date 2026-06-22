from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy

# Generic Views
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from .models import Note

class NoteListView(ListView):
	model = Note
	template_name = "notes/note_list_view.html"
	context_object_name = "notes"
	paginate_by = 1

class DetailView(DetailView):
	model = Note
	template_name = "notes/note_detail.html"

class NoteCreateView(CreateView):
	model = Note
	fields = ["title", "content"]
	template_name = "notes/note_form.html"
	success_url = reverse_lazy("list")

class NoteUpdateView(UpdateView):
	model = Note
	fields = ["title", "content"]
	template_name = "notes/note_update_view.html"
	success_url = reverse_lazy('list')


class NoteDeleteView(DeleteView):
	model = Note
	fields = ["title", "content"]
	template_name = "notes/confirm_delete.html"
	success_url = reverse_lazy('list')

def home_view(request):
	if request.method == "GET":
		return HttpResponse("Welcome to Home Page")

class HomeView(View):

	def get(self, request):
		return HttpResponse("Welcome to Home Page from CBV")

