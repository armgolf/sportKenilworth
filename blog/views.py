from django.shortcuts import render
from blog.models import Clubs, Events

def club_list(request):
    clubs = Clubs.objects.all()
    return render(request, 'blog/club_list.html', {'clubs': clubs,})

def event_list(request):
    events = Events.objects.all()
    return render(request, 'blog/event_list.html', {'events': events,})

def contact(request):
    return render(request, 'blog/contact.html', {'contact': contact,})
