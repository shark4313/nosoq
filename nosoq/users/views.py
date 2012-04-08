# Create your views here.

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from users.forms import *
from django.template import RequestContext
#ajax request 
def feed_models(request, city_id):    
    city = City.objects.get(pk=city_id)  
    teams = Team.objects.filter(city=city)     
    return render_to_response('teamSelection.html', {"city_id":city_id,'teams':teams}, )

def handle(request):
    if request.method == 'POST':
         artists = request.POST.getlist('artists') 
         # now artists is a list of [1,2,3]

         
def add_classified(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
    if request.POST.has_key('city'):
        model_id = request.POST['city']
    else:
        model_id = 0
    return render_to_response('test.html', {'form':form,'model_id':model_id}, context_instance=RequestContext(request))
