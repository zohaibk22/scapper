from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    page = requests.get('https://www.google.com')
    soup = BeautifulSoup(page.content, 'html.parser')
    link_address = []

    for link in soup.find_all('a'):
        link_address.append(link.get('href'))

    return render(request=request, template_name='scapper/index.html', context={'links': link_address})