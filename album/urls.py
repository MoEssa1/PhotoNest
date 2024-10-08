from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('welcome/', views.WelcomePage, name='welcome'),
    path('welcome/tag/<str:tag_name>/', views.WelcomePage, name='photos_by_tag'),
    path('photo/<int:id>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('photo/<int:id>/edit/', views.updatePhoto, name='update'),
    path('photo/<int:id>/delete/', views.deletePhoto, name='delete')
]
