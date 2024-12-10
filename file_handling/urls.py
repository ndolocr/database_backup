from django.urls import path

from file_handling import views

urlpatterns = [
    path("access/<str:folder_name>", views.access_folder_contents, name="access_folder_contents"),
]