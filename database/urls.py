from django.urls import path

from database import views

urlpatterns = [
    path('get/<str:table_name>/table/structure', views.get_table_structure),
    path('archive/<str:table_name>/table/structure', views.archive_table_structure),
]