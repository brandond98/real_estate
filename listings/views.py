from django.shortcuts import render
from .models import Listing
# Create your views here.

def index(request):
    listings = Listing.objects.all()
    context = {
        'listings' : listings
    }
    return render (request, 'apps/listings/listings.html', context)

def listing(request):
    return render (request, 'apps/listings/listing.html')

def search(search):
    return render (request, 'apps/listings/search.html')