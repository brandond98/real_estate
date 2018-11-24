from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings' : paged_listings
    }
    return render (request, 'apps/listings/listings.html', context)

def listing(request, listing_id):
    return render (request, 'apps/listings/listing.html')

def search(search):
    return render (request, 'apps/listings/search.html')
