from django.urls import path
from .views import list_paciente, create_paciente, update_paciente, delete_paciente

urlpatterns = [
    path('', list_paciente, name='list_paciente'),
    path('new', create_paciente, name='create_paciente'),
    path('update/<int:id>/', update_paciente, name='update_paciente'),
    path('delete/<int:id>/', delete_paciente, name='delete_paciente'),
]


# CRUD - CREATE, READ, UPDATE, DELETE