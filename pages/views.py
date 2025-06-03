from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    """Render the home page."""
    return render(request, 'pages/home.html', {'welcome_message': 'Welcome to our restaurant! '})


def about(request):
    """Render the about page."""
    return render(request, 'pages/about.html')


@login_required
def member_page(request):
    return render(request, 'pages/member.html', {"user": request.user})
