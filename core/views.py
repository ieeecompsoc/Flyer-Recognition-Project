from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
import json
from .models import Event
# Create your views here.
import requests

def HomeView(request):
	if request.method == "POST":
		image = request.POST.get('image')

		response = requests.post('http://demo2457258.mockable.io/flyer_recognition')
		response = response.json()
		print(response)
		context = {
			'name_of_event': response['name_of_event'],
			'hosted_by': response['hosted_by'],
			'date_of_event' : response['date_of_event'],
			'time_of_event': response['time_of_event'],
			'location': response['location']
		}
		return render(request, "core/preview.html", context)
	else:
		context = {}
		return render(request, 'core/homeview.html', context)

def SaveData(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		date = request.POST.get('date')
		time = request.POST.get('time')
		location = request.POST.get('location')
		hosted_by = request.POST.get('hosted_by')

		temp = Event.objects.create(name=name, date=date, time=time, location=location, hosted_by=hosted_by)
		return redirect('viewevents')

def ViewEvents(request):
	events = Event.objects.all()
	context = {
		'events': events
	}

	return render(request, 'core/viewevents.html', context)