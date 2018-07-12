from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from django.shortcuts import render   # Added for this step

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        {
            'title': "Hello Django",
            'content': " Hello Django!", 
            'message': " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )