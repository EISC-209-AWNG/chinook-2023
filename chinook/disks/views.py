from django.http import HttpResponse


def album_list(request):
    return HttpResponse("List of albums coming soon.")

def album_details(request, album_id):
    return HttpResponse("Details of album with id=%s coming soon." % album_id)