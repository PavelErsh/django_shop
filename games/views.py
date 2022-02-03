from django.shortcuts import render
from django.views.generic import ListView

from games.models import Game

class GameListView(ListView):
    model = Game
    
#test 
# Create your views here.
def home(request):
    return render(request, 'home.html')

