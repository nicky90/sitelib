from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'diglib/index.html', {})
    #return HttpResponse("This is the Oracle Library Home Page.")

def search(request):
    return HttpResponse("This is the Oracle Library Search Page.")

def search_results(request):
    return HttpResponse("This is the Oracle Library Search Results Page.")


