from django.urls import reverse
from django.http import Http404
from django.views.generic import ListView
from django.shortcuts import render, redirect
#from django.core.paginator import Paginator,EmptyPage

from rooms.models import Room

class HomeView(ListView):
    model            = Room
    paginate_by      = 10
    paginate_orphans = 5
    ordering         = "created_at"
    context_object_name = "rooms"

def room_detail(request, pk):
    try:
        room = Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except Room.DoesNotExist:
        raise Http404()
        #return redirect(reverse("core:home"))









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

