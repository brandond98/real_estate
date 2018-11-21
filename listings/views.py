from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'apps/listings/listings.html')

def listing(request):
    return render (request, 'apps/listings/listing.html')

def search(search):
    return render (request, 'apps/listings/search.html')