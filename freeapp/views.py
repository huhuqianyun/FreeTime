from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, "freeapp/index.html")

def about(request):
    return render(request, 'freeapp/about.html')

def attend_activities(request):
    return render(request, 'freeapp/attend_activities.html')

def organize_activities(request):
    return render(request, 'freeapp/organize_activities.html')

def myhome(request):
    return render(request, 'freeapp/myhome.html')

