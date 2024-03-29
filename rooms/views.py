from django.urls import reverse
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django_countries import countries

from rooms.models import Room, RoomType, Amenity, Facility
from rooms.forms import SearchForm

class HomeView(ListView):
    model            = Room
    paginate_by      = 12
    paginate_orphans = 5
    ordering         = "created_at"
    context_object_name = "rooms"

class RoomDetail(DetailView):
    model = Room

class SearchView(View):
    def get(self, request):
        country = request.GET.get("country")

        if country:
            form = SearchForm(request.GET)

            if form.is_valid():
                city         = form.cleaned_data.get("city")
                country      = form.cleaned_data.get("country")
                room_type    = form.cleaned_data.get("room_type")
                price        = form.cleaned_data.get("price")
                guests       = form.cleaned_data.get("guests")
                bedrooms     = form.cleaned_data.get("bedrooms")
                beds         = form.cleaned_data.get("beds")
                bathrooms    = form.cleaned_data.get("bathrooms")
                instant_book = form.cleaned_data.get("instant_book")
                superhost    = form.cleaned_data.get("superhost")
                amenities    = form.cleaned_data.get("amenities")
                facilities   = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if bathrooms is not None:
                    filter_args["bathrooms__gte"] = bathrooms

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                querySet = Room.objects.filter(**filter_args).order_by("created_at")

                paginator = Paginator(querySet, 10, orphans=5)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)

                return render(request, "rooms/search.html", {"form": form, "rooms": rooms})
        else:
            form = SearchForm()

        return render(request, "rooms/search.html", {"form": form})

