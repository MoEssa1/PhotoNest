from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# class HomePage(TemplateView):
#     """
#     Displays home page'
#     """
#     template_name = 'index.html'

def HomePage(request):
    return render(request, 'album/index.html')

def WelcomePage(request):
    return render(request, 'album/welcome_page.html')