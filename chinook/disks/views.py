from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .forms import SearchForm
from .models import Album

def album_list(request):
    """
    Get albums from database, either all of them or those matching a POST request
    :param request: The incoming request
    """
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            albums = Album.objects.filter(title__contains=query)
        else:
            albums = get_list_or_404(Album)
    else:
        search_form = SearchForm()
        albums = get_list_or_404(Album)
    return render(request, 'disks/album_list.html', {'albums': albums, 'form': search_form})

def album_details(request, album_id):
    """
    Get the specified album
    :param request: The incoming request
    :param album_id: The album's ID
    """
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'disks/album_details.html', {'album': album})
