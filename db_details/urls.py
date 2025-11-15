from django.urls import path
from db_details import views

urlpatterns = [
    path(route='db-check/', view=views.db_check, name='db_check')
]