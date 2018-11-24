from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings  = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }

    return render(request, 'apps/pages/index.html', context)

def about(request):
    realtors = Realtor.objects.all()
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {

        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }

    return render(request, 'apps/pages/about.html', context)
