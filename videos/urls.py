from django.urls import path
from . import views

app_name='videos'
urlpatterns = [
    path('upload/', views.upload_video, name='upload_video'),
    path('all/', views.view_videos, name='view_videos'),
    path('', views.dashboard, name='dashboard'),
    path('my/', views.my_profile, name='my_profile'),
    
    
]
