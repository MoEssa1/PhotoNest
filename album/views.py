from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Tag, Photo, Profile 



def HomePage(request):
    return render(request, 'album/index.html')

@login_required
def WelcomePage(request, tag_name=None):
    tags = Tag.objects.all()
    photos_list = None

    if tag_name:
        tag_name = tag_name.lower()
        selected_tag = get_object_or_404(Tag, name__iexact=tag_name)
        photos_list = Photo.objects.filter(tags=selected_tag).order_by('-date_uploaded')
    else:
        photos_list = Photo.objects.all().order_by('-date_uploaded')
    
    paginator = Paginator(photos_list, 6)
    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    
    context = {
        'tags':tags, 
        'photos':photos, 
        'is_paginated': photos.has_other_pages(),
        'page_obj': photos,
        'selected_tag': selected_tag if tag_name else None 
        }
    return render(request, 'album/welcome_page.html', context)

# to view photo write function to get photo
def viewPhoto(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, 'album/photo.html', {'photo': photo})

# This function will allow user to upload a photo to the album
@login_required
def addPhoto(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        selected_tag_ids = request.POST.getlist('tags')
        tags_to_add = []

        for tag_id in selected_tag_ids:
            selected_tag = Tag.objects.get(id=tag_id)
            tags_to_add.append(selected_tag)

        new_tag_name = data.get('tags_new', '')
        if new_tag_name:
            new_tag, created = Tag.objects.get_or_create(name=new_tag_name)
            tags_to_add.append(new_tag)


        # Get the profile of the logged-in user
        profile = get_object_or_404(Profile, user=request.user)

        if image:
            photo = Photo.objects.create(
                profile=profile,
                caption=data.get('caption', ''),
                image=image,
            )

            if tags_to_add:
                photo.tags.set(tags_to_add)

        return redirect('welcome')

    context = {'tags':tags}
    return render(request, 'album/add_photo.html', context)


# This function will allow users to update photos uploaded by themselves
@login_required
def updatePhoto(request, id):
    photo = get_object_or_404(Photo, id=id, profile__user=request.user)

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        selected_tag_ids = request.POST.getlist('tags')
        tags_to_add = []

        for tag_id in selected_tag_ids:
            selected_tag = Tag.objects.get(id=tag_id)
            tags_to_add.append(selected_tag)
        
        new_tag_name = data.get('tags_new', '')
        if new_tag_name:
            new_tag, created = Tag.objects.get_or_create(name=new_tag_name)
            tags_to_add.append(new_tag)     

        if image:
            photo.image = image

        photo.caption = data.get('caption', '')

        if tags_to_add:
            photo.tags.set(tags_to_add)

        photo.save()

        return redirect('welcome')

    tags = Tag.objects.all()
    context = {'photo': photo, 'tags': tags}
    return render(request, 'album/update_photo.html', context)


# This function will allow users to delete previously uploaded photo's
@login_required
def deletePhoto(request, id):
    photo = get_object_or_404(Photo, id=id, profile__user=request.user)

    if request.method == 'POST':
        photo.delete()
        return redirect('welcome')

    context = {'photo': photo}
    return render(request, 'album/delete_photo.html', context)