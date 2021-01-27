from django.shortcuts import render
import datetime

from scraping.Models.JobAD.JobAd import JobAd
from scraping.forms import FinderForm


def home(request):
    form = FinderForm()
    # city = request.POST['city']
    # branch = request.POST['branch']
    print(request.POST)
    # if city or branch:
    #     _filter = {}
    #     if city:
    #         _filter['city__id'] = city
    #     if branch:
    #         _filter['occupation__id'] = branch
    #     qs = JobAd.objects.filter(** _filter)
    # else:

    qs = JobAd.objects.all()

    return render(request, 'scraping/home.html', {'object_list': qs, 'form': form})
