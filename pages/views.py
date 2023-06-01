from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, state_choices, price_choices
# Create your views here.
def index(request):
    
    listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings, 3)
    pag_number = request.GET.get("page")
    
    page_listing = paginator.get_page(pag_number)
    
    context = {
        "listings": page_listing,
        "bedroom_choices": bedroom_choices,
        "state_choices":state_choices,
        "price_choices":price_choices,
    }
    
    return render(request,'pages/index.html',context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # Get mvp realtors 
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    
    context = {
        "realtors": realtors,
        "mvp_realtor": mvp_realtor
    }
    return render(request, 'pages/about.html',context)