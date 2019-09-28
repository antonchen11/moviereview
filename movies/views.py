from django.shortcuts import render, redirect
from django.contrib import messages
from airtable import Airtable #google spreadsheet on steroids
import os # using for environment vars

#Connect to airtable database
AT = Airtable(os.environ.get('AIRTABLE_MOVIESTABLE_BASE_ID'),
                'Movies',
                api_key=os.environ.get('AIRTABLE_API_KEY'))

# Create your views here.
#homepage is a funciton that takes in the request as an argument.
#render that request and show/run the following html file.
def home_page(request):
    # print(str(request.GET.get('query', '')))
    user_query = str(request.GET.get('query', '')) #Get method and pull from html text box of query
    search_result = AT.get_all(formula="FIND('" + user_query.lower() + "', LOWER({Name}))")
    stuff_for_frontend = {'search_result': search_result} #context dictionary of K:V
    return render(request, 'movies/movies_stuff.html', stuff_for_frontend)
    
    # Connect the above path under urls.py
    
#function that takes information from create form and push to back end.    
def create(request):  
    print('haha')
    return redirect('/')
