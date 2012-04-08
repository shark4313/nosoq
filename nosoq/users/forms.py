
from django import forms
from django.utils.translation import ugettext as _

from users.models import *

#normal char feild but save data 
class DynamicChoiceField(forms.ChoiceField): 
   def clean(self, value):        
        return value


    
    # def __init__(self,  *args, **kwargs):
        # super(searchForm, self).__init__(*args, **kwargs)

        # city_list = []
        # for m in City.objects.all():
            # city_list.append( ( m.pk, m.name ) )
        
        # team_list = []
        # for b in Team.objects.all():
            # team_list.append( (b.pk, b.name)  )
        
        # team_choices = tuple(team_list)
        # city_choices = tuple(city_list) # tuple of tuple
        
        # self.fields['team'].choices=team_choices
        # self.fields['city'].choices=city_choices
       