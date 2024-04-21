from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def myView(request):
	return HttpResponse('Hello World!')

def kiosk(request):
	return render(request, 'Kiosk/kiosk.html')

def kitch(request):
	return render(request, 'kiosk/kitch.html')