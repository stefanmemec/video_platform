from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video
from django.contrib.auth.decorators import login_required

@login_required
def upload_video(request):
    """View to upload a new video"""
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('videos:dashboard')
    else:
        form = VideoForm()
    return render(request, 'videos/upload_video.html', {'form': form})

@login_required
def view_videos(request):
    """View all videos"""
    videos = Video.objects.all().order_by('-uploaded_at')
    return render(request, 'videos/view_videos.html', {'videos': videos})

@login_required
def dashboard(request):
    """Dashboard showing all videos (could add stats later)"""
    videos = Video.objects.all().order_by('-uploaded_at')
    return render(request, 'videos/dashboard.html', {'videos': videos})

@login_required
def my_profile(request):
    """Shows only videos uploaded by the logged-in user"""
    my_videos = Video.objects.filter(user=request.user).order_by('-uploaded_at')

    # Optional: include an upload form on the profile page
    form = VideoForm()

    return render(request, 'videos/my_profile.html', {
        'videos': my_videos,
        'form': form,  # send form if you want uploads here
    })
