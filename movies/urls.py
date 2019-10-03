from django.urls import path #django pathing module
from . import views #add the views its going to connect to

#look for the views.home_page function and run in
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create/', views.create, name='create'),
    path('edit/<str:movie_id>', views.edit, name='edit'),
    path('delete/<str:movie_id>', views.delete, name='delete'),
]

