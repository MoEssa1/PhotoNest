from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Tag, Photo 

# Create your views here.
# class HomePage(TemplateView):
#     """
#     Displays home page'
#     """
#     template_name = 'index.html'

def HomePage(request):
    return render(request, 'album/index.html')

def WelcomePage(request):
    tags = Tag.objects.all()
    photos = Photo.objects.all()
    context = {'tags':tags, 'photos':photos}
    return render(request, 'album/welcome_page.html', context)

# to view photo write function to get photo
def viewPhoto(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, 'album/photo.html', {'photo': photo})