from django.urls import reverse
#from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
#from django.core.paginator import Paginator,EmptyPage

from django_countries import countries

from rooms.models import Room, RoomType, Amenity, Facility

class HomeView(ListView):
    model            = Room
    paginate_by      = 10
    paginate_orphans = 5
    ordering         = "created_at"
    context_object_name = "rooms"

class RoomDetail(DetailView):
    model = Room

def search(request):
    city                = request.GET.get("city", "Anywhere")
    city                = str.capitalize(city)
    country             = request.GET.get("country", "KR")
    room_type           = int(request.GET.get("room_type", 0))
    price               = int(request.GET.get("price", 0))
    guests              = int(request.GET.get("guests", 0))
    bedrooms            = int(request.GET.get("bedrooms", 0))
    beds                = int(request.GET.get("beds", 0))
    bathrooms           = int(request.GET.get("bathrooms", 0))
    instant             = bool(request.GET.get("instant", False))
    superhost          = bool(request.GET.get("superhost", False))
    selected_amenities  = request.GET.getlist("amenities")
    selected_facilities = request.GET.getlist("facilities")

    form = {"city"             : city, "selected_room_type" : room_type,
            "selected_country" : country, "price"           : price,
            "guests"           : guests, "bedrooms"         : bedrooms,
            "beds"             : beds, "bathrooms"          : bathrooms,
            "selected_amenities" : selected_amenities,
            "selected_facilities" : selected_facilities,
            "instant" : instant,
            "superhost" : superhost
            }

    room_types = RoomType.objects.all()
    amenities = Amenity.objects.all()
    facilities = Facility.objects.all()

    choices = {"countries" : countries,
               "room_types": room_types,
               "amenities" : amenities,
               "facilities": facilities
              }
    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk__exact"] = room_type

    if price != 0:
        filter_args["price__lte"] = price
    if guests != 0:
        filter_args["guests__gte"] = guests
    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms
    if beds != 0:
        filter_args["beds__gte"] = beds
    if bathrooms != 0:
        filter_args["bathrooms__gte"] = bathrooms
    if instant is True:
        filter_args["instant_book"] = True
    if superhost is True:
        filter_args["host__superhost"] = True
    if len(selected_amenities) > 0:
        for selected_amenity in selected_amenities:
            filter_args["amenities__pk"] = int(selected_amenity)
    if len(selected_facilities) > 0:
        for selected_amenity in selected_facilities:
            filter_args["facilities__pk"] = int(selected_amenity)

    rooms = Room.objects.filter(**filter_args)

    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})


    """ - Function Based View (FBV)
def room_detail(request, pk):
    try:
        room = Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except Room.DoesNotExist:
        #raise Http404()
        return redirect(reverse("core:home"))
    """








    """ #1. function-based view
    def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)

    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")
    """

    """ #2 Without django tool, pagination is created
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = Room.objects.all()[offset:limit]
    page_count = ceil(Room.objects.count() / page_size)
    page_range = range(0, page_count)

    return render(request, "rooms/home.html", {
                    "rooms": all_rooms,
                    "page": page,
                    "page_count" : page_count,
                    "page_range" : page_range
                    }
                 )
"""

