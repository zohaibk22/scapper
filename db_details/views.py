from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections

# Create your views here.
def db_check(request):
    try: 
        connections['default'].cursor()
        return HttpResponse("Database connection successful.")
    except Exception as e:
        return HttpResponse(f"Database connection failed: {e}")