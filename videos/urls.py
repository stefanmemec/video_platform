from django.urls import path
from . import views

app_name = "videos"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("upload/", views.upload_video, name="upload_video"),
    path("my/", views.my_profile, name="my_profile"),
]
