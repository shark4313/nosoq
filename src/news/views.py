from forms import NewsForm
from django.shortcuts import render_to_response

#def add_news_item(request):
#    if request.method == 'GET':
#        form = NewsForm()
#        return render_to_response('add_news.html', {'from':from})
#    else request.method == 'POST':
#        form = NewsForm(data=request.POST)