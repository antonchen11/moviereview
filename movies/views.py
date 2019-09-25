from django.shortcuts import render
from django.contrib import messages
from airtable import Airtable #google spreadsheet on steroids
import os # using for environment vars

# Create your views here.
#homepage is a funciton that takes in the request as an argument.
#render that request and show/run the following html file.
def home_page(request):
    return render(request, 'movies/movies_stuff.html')
    
# Connect the above path under urls.py
    
    

