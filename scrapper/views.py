from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link

# Create your views here.
def index(request):
    url = ''
    if request.method == 'POST':
        url = request.POST.get('url', '')
    if url:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        link_address = []

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.get_or_create(website_name=url, address=link_address, name=link_text)

        data = Link.objects.filter(website_name=url)
    else:
        data = []

    return render(request=request, template_name='scrapper/index.html', context={'links': data})