from django.db import models
import urllib.request
import urllib
import json
from urllib.parse import quote

# Create your models here.

class Movie(models.Model):

	title = models.TextField()


	def getMovieData(self, title):
		#jsonData = urllib.request.urlopen("http://omdbapi.com/?t=%s&y=&tomatoes=true&plot=short&r=json" % title)
		#request = urllib.request.Request("http://omdbapi.com/?t=%s&y=&tomatoes=true&plot=short&r=json" % title)
		#response = urllib.request.urlopen(request)
		title = urllib.parse.quote(title)

		request = urllib.request.Request("http://omdbapi.com/?t=%s&y=&tomatoes=true&plot=short&r=json" % title)
		response = urllib.request.urlopen(request)
		json_string = response.read().decode('utf-8')

		moviedict = json.loads(json_string)
		self.movieData = {}
		if(moviedict['Response'] == 'True'):
			self.movieData['title'] = moviedict['Title']
			self.movieData['year'] = moviedict['Year']
			if moviedict['imdbRating'] != "N/A":
				self.movieData['userrating'] = round(float(moviedict['imdbRating']) * 10)
				if moviedict['tomatoUserRating'] != "N/A":
					self.movieData['userrating'] = round((float(moviedict['imdbRating']) + (float(moviedict['tomatoUserRating']) * 2)) * 5)
			self.movieData['imdbID'] = moviedict['imdbID']
			self.movieData['language'] = moviedict['Language']
			self.movieData['plot'] = moviedict['Plot']
			self.movieData['genres'] = moviedict['Genre'].split(',')
			self.movieData['posterURL'] = self.generateImageLink(moviedict['imdbID'])
			
		self.movieData['response'] = moviedict['Response']
		return self.movieData

	def generateImageLink(self, imdbid):
		imageURL = 'http://img.omdbapi.com/?i=' + imdbid + '&apikey=8d8ace5a&h=275'
		return imageURL

