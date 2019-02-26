from django.shortcuts import render
from django.http import HttpResponse
from .models import Fertilizer

# Create your views here.

def home(request):
	fertilizers = Fertilizer.objects.all()
	return render(request,'home.html',{'fertilizers':fertilizers})
def details(request):
	fertilizers = Fertilizer.objects.all()
	
    query = request.GET.get('fert_name')

    if query:

        fertilizers = fertilizers.filter(name__contains=query)

    context = {
            'fert_name' : fert_name
        }


	return render(request, 'details.html', context)






