from django.shortcuts import render
from .Models.JobAD.JobAd import JobAd


def home(request):
    qs = JobAd.objects.all()
    return render(request, 'home.html', {'object_list': qs})
    # Create your views here.
