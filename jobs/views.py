from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

    
def baba(request):
    return render(request, 'jobs/baba.html')