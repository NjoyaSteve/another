from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="animouth-index"),
    path("about/", views.about, name="animouth-about"),
]