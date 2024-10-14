from alumno import views
from django.urls import path

urlpatterns = [
    path("",views.index_vista,name="index_vista")
]