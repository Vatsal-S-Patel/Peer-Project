from django.shortcuts import render
from django.http import HttpResponse

from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    return HttpResponse(profiles)

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact='')
    other_skills = profile.skill_set.filter(description='')
    return HttpResponse(profile)