from django.shortcuts import render
from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request, 'home.html', {
        'jobs': jobs
    })

    
def baba(request):
    return render(request, 'jobs/baba.html')