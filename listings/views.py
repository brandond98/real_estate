from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from realtors.models import Realtor

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
    listing = get_object_or_404(Listing, pk=listing_id)
    realtors = Realtor.objects.all()
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'listing': listing,
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }

    return render(request, 'apps/listings/listing.html', context)

def search(search):
    return render(request, 'apps/listings/search.html')


realtors = Realtor.objects.all()
mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
context = {


}