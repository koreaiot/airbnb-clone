from . import models
from django.shortcuts import render


def all_rooms(request):
    all_rooms = models.Room.objects.all()[:5]
    return render(request, "rooms/home.html", context={"potato": all_rooms})
