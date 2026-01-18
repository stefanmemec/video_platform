from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cloudinary.utils import cloudinary_url

from .models import Video
from .forms import VideoForm


@login_required
def dashboard(request):
    videos = Video.objects.all().order_by("-uploaded_at")

    for video in videos:
        video.video_url = cloudinary_url(
            video.file.public_id,
            resource_type="video",
            format="mp4"
        )[0]

    return render(request, "videos/dashboard.html", {
        "videos": videos
    })


@login_required
def upload_video(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect("videos:dashboard")
    else:
        form = VideoForm()

    return render(request, "videos/upload_video.html", {
        "form": form
    })


@login_required
def my_profile(request):
    videos = Video.objects.filter(user=request.user).order_by("-uploaded_at")
    form = VideoForm()

    return render(request, "videos/my_profile.html", {
        "videos": videos,
        "form": form
    })
