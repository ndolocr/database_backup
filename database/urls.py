from django.urls import path

from database import views

urlpatterns = [
    path('rules/table/<str:table_name>', views.get_table_structure),
]