from django.urls import path
from . import views

app_name = "ministries"

urlpatterns = [
    path("", views.ministry_list, name="list"),
]
