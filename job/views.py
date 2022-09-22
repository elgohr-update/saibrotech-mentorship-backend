from unicodedata import category
from job.models import Category, Job
from django.shortcuts import render


def index(request):

    if 'search' in request.GET:
        search = request.GET['search']
        jobs = Job.objects.filter(title__icontains=search)
    else:
        jobs = Job.objects.all()

    areas = Category.objects.all()

    if 'area' in request.GET:
        area = request.GET['area']
        jobs = Job.objects.filter(category__code=area)
    else:
        jobs = Job.objects.all()

    context = {
        'areas': areas,
        'jobs': jobs
    }
    return render(request, 'job/index.html', context)