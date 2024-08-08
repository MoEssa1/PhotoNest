from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tag, Photo, Profile 



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

@login_required
def addPhoto(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        selected_tag_id = data.get('tags', 'none')
        new_tag_name = data.get('tags_new', '')

        tags_to_add = []

        if selected_tag_id != 'none':
            selected_tag = Tag.objects.get(id=selected_tag_id)
            tags_to_add.append(selected_tag)
        elif new_tag_name != '':
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
                photo.tags.set(tags_to_add)  # Add tags to the photo

        return redirect('welcome')

    context = {'tags':tags}
    return render(request, 'album/add_photo.html', context)