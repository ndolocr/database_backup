from django.urls import path

from file_handling import views

urlpatterns = [
    path("access/<str:folder_name>", views.desktop_folder_contents, name="desktop_folder_contents"),
]