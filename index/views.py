from django.shortcuts import render
from index.models import *


# Create your views here.

def homepage(request):
	return render(request, 'index/home.html')

def results(request):
	m = Movie()
	if request.GET.get('q') is not None:
		searchname = request.GET.get('q')
		movieData = m.getMovieData(searchname)
		return render(request, 'index/home.html', {'movieData': movieData, 'search': True})
	else:
		return render(request, 'index/home.html')
	#print (searchname)
	