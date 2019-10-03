from django.shortcuts import render, redirect
from django.contrib import messages # FOR NOTIFICATIONS YO!
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
    # print(search_result)
    # print(stuff_for_frontend)
    return render(request, 'movies/movies_stuff.html', stuff_for_frontend)
    
    # Connect the above path under urls.py
    
#function that takes information from create form and push to back end.    
def create(request):  
    if request.method == 'POST':
        data = {
            'Name': request.POST.get('name'),
            'Pictures': [{'url': request.POST.get('url') or 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiZ9uru0krqOeB9wniwCrYy-jWFdB7LVtjF41Fm9cpBhXPzVyx' }],
            'Rating': int(request.POST.get('rating')),
            'Notes': request.POST.get('notes'),            
        }

        try:
            response = AT.insert(data)
            messages.success(request, 'New Movie Added: {}'.format(response['fields'].get('Name')))
        except Exception as e:
            messages.warning(request, 'Got an error when trying to create a new movie: {}').format(e)
        
    return redirect('/')

def edit(request, movie_id):
    if request.method == 'POST':
        data = {
            'Name': request.POST.get('name'),
            'Pictures': [{'url': request.POST.get('url') or 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiZ9uru0krqOeB9wniwCrYy-jWFdB7LVtjF41Fm9cpBhXPzVyx' }],
            'Rating': int(request.POST.get('rating')),
            'Notes': request.POST.get('notes'),
        }
        
        try:
            response = AT.update(movie_id, data)
            #notify on updaate
            messages.success(request, 'New Movie Updated: {}'.format(response['fields'].get('Name')))
        except Exception as e:
            messages.warning(request, 'Got an error when trying to update a movie: {}').format(e)
        
    return redirect('/')
    
def delete(request, movie_id):
    try:
        movie_name = AT.get(movie_id)['fields'].get('Name')
        AT.delete(movie_id)
        #notify on delete
        messages.warning(request, 'Deleted movie: {}'.format(movie_name))
    except Exeception as e:
        messages.warning(request, 'Got an error trying to delete a movie: {}').format(e)
    return redirect('/')
    
#notify ppl when they create,edit or delete a movie


    
