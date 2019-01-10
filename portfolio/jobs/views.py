from django.shortcuts import render
from .models import Job

# Create your views here.
def nick(request):
    return render(request, 'jobs/home.html')

def homepage(request):
    return render(request, 'jobs/home.html')
