from django.forms import ModelForm
from models import NewsItem

# Create the form class.
class NewsForm(ModelForm):
   class Meta:
       model = News
