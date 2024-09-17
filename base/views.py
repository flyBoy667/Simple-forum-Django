from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

rooms = [
    {
        'id': 1,
        'name': 'Lets learn python'
    },
    {
        'id': 2,
        'name': 'Design with me'
    },
    {
        'id': 3,
        'name': 'Fronted devs'
    }
]


def home(request):
    return render(request, "base/home.html", {'rooms': rooms})


def room(request, pk: str):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    return render(request, "base/room.html", {'room': room})
