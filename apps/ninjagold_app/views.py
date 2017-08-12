# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    try: request.session['gold']
    except: request.session ['gold'] = 0
    try: request.session['activity']
    except: request.session ['activity'] = []
    return render (request, 'index.html')

def process(request):
    if (request.POST['place'] == 'casino'):
        request.session['gold'] -= 10 #make this a random number negative or positive from -50 to 50
        request.session['activity'].append("You entered the casino, played a few games and lost 10 gold.")
    if (request.POST['place'] == 'farm'):
        request.session['gold'] += 10 #make this a random number negative or positive from -50 to 50
        request.session['activity'].append("You entered the farm, searched the ground and found 10 gold!")
    if (request.POST['place'] == 'house'):
        request.session['gold'] += 0 #make this a random number negative or positive from -50 to 50
        request.session['activity'].append("You broke in and entered the house, rummaged around and found nothing.")
    if (request.POST['place'] == 'junkyard'):
        request.session['gold'] += 25 #make this a random number negative or positive from -50 to 50
        request.session['activity'].append("You entered the junkyard, dug around and found 25 gold!")

    return redirect ('/')
