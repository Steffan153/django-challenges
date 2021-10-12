from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse

months = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!",
}

def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponse:
    try:
        return HttpResponseRedirect(reverse('month-challenge', args=[list(months.keys())[month - 1]]))
    except Exception:
        return HttpResponseNotFound("Invalid month number!")

def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    if month not in months:
        return HttpResponseNotFound("Invalid month!")
    return HttpResponse(months[month])