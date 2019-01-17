from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from realtors.models import Realtor
from .choices import price_choices, bedroom_choices, county_choices

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

    context = {
        'listing': listing,
    }

    return render(request, 'apps/listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #County
    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            queryset_list = queryset_list.filter(county__iexact=county)

    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'county_choices': dict((x, y) for x, y in county_choices),
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'apps/listings/search.html', context)


realtors = Realtor.objects.all()
mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
context = {


}