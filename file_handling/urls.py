from django.urls import path

from file_handling import views

urlpatterns = [
    path("desktop/folder/contents", views.desktop_folder_contents, name="desktop_folder_contents"),
]