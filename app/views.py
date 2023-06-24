from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    accessrecords=AccessRecord.objects.all()
    d={'accessrecords':accessrecords}
    return render(request,'display_AccessRecord.html',d)