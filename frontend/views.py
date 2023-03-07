from django.shortcuts import render

# Create your views here.

# We need to render the index template and then let react take care of it and start rendering things inside of this. 

def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html') 

# the render will take the request, take the template and it will simply return that HTML to whatever sent the request
 