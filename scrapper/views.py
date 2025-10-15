from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link

# Create your views here.
def index(request):
    page = requests.get('https://www.google.com')
    soup = BeautifulSoup(page.content, 'html.parser')
    
    link_address = []

    for link in soup.find_all('a'):
        link_address = link.get('href')
        link_text = link.string
        Link.objects.get_or_create(address=link_address, name=link_text)

    data = Link.objects.all()

    return render(request=request, template_name='scapper/index.html', context={'links': data})