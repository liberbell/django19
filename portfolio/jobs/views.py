from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def nick(request):
    return render(request, 'jobs/home.html')

def homepage(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
    # print(job_id)
    job_detail = get_object_or_404(jobs, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})
