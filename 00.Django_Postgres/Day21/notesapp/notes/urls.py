from django.urls import path
from .views import home_view, HomeView, NoteListView, DetailView, NoteCreateView
from .views import NoteUpdateView, NoteDeleteView

urlpatterns = [
    # path('', home_view, name="home"),
    path('', HomeView.as_view(), name='home_cbv'),
    path('list', NoteListView.as_view(), name="list"),
    path('detail/<int:pk>', DetailView.as_view(), name='details'),
    path('create', NoteCreateView.as_view(), name="create"),
    path('update/<int:pk>', NoteUpdateView.as_view(), name="update-view"),
    path("delete/<int:pk>", NoteDeleteView.as_view(), name="delete-view")
]
