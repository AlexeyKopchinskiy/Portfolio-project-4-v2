from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    """Render the home page."""
    return render(request, 'home.html', {'welcome_message': 'Welcome to our restaurant! '})


def about(request):
    """Render the about page."""
    return render(request, 'about.html')


@login_required
def member_page(request):
    return render(request, 'member.html', {"user": request.user})
