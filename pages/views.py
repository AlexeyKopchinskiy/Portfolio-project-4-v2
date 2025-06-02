from django.shortcuts import render

# Create your views here.


def home(request):
    """Render the home page."""
    return render(request, 'pages/home.html', {'welcome_message': 'Welcome to my site!'})


def about(request):
    """Render the about page."""
    return render(request, 'pages/about.html')
