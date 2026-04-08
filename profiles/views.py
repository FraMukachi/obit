from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
from .matching import find_matches
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
@csrf_exempt
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile.age = request.POST.get('age')
        profile.bio = request.POST.get('bio')
        profile.interests = request.POST.get('interests')
        profile.location = request.POST.get('location')
        profile.save()
        return redirect('dashboard')
    
    return render(request, 'profile.html', {'profile': profile})

@login_required
def matches_view(request):
    all_profiles = Profile.objects.exclude(user=request.user)
    matches = find_matches(request.user, all_profiles)
    return render(request, 'matches.html', {'matches': matches})
