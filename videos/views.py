from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video
from django.contrib.auth.decorators import login_required

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user  # assign the logged-in user
            video.save()
            return redirect('videos:dashboard')  # враќа на dashboard
    else:
        form = VideoForm()
    return render(request, 'videos/upload_video.html', {'form': form})

@login_required
def view_videos(request):
    videos = Video.objects.all().order_by('-uploaded_at')
    return render(request, 'videos/view_videos.html', {'videos': videos})


@login_required
def dashboard(request):
    videos = Video.objects.all().order_by('-uploaded_at')  # сите видеа, за All Videos
    return render(request, 'videos/dashboard.html', {'videos': videos})


@login_required
def my_profile(request):
    my_videos = Video.objects.filter(user=request.user).order_by('-uploaded_at')

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('videos:my_profile')
    else:
        form = VideoForm()

    return render(request, 'videos/my_profile.html', {'videos': my_videos})
