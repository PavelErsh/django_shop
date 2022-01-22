from django.shortcuts import render
#test 
# Create your views here.
def home(request):
    return render(request, 'home.html')
