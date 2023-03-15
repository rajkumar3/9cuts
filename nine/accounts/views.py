from django.shortcuts import render
from cuts import templates
# Create your views here.

def index(request):
	return render(request, 'cuts/home.html')