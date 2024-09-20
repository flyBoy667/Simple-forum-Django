from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from base.forms import RoomForm
from base.models import Room, Topic


# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    return render(request, "base/home.html", {"rooms": rooms, "topics": topics})


def room_detail(request, pk: str):
    room = Room.objects.get(id=pk)
    return render(request, "base/room.html", {"room": room})


def create_room(request):
    form = RoomForm()
    context = {"form": form}

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, "base/room_form.html", context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/room_delete.html', {"room": room})
