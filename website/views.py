from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meeting_planner.meetings.models import Meeting


def welcome(request):
    return  render(request, "website/welcome.html",
            {"num_meetings": Meeting.objects.count()})


def date(request):
    return HttpResponse("This page was served at" + str(datetime.now()))

def about(request):
    return  HttpResponse("I'm reindert and I make courses for Pluralsight my name is keerthan.")
