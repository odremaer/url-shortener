from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import URL

from .forms import URLForm
from django.http import QueryDict

def home(request):
    return render(request, 'shortenerapp/home.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = URLForm(request.POST)
        full_url = request.POST['full_url']
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            url = URL()
            return HttpResponse(str(url.url_hash))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = URLForm()

    return render(request, 'shortenerapp/home.html', {'form': form})


def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    return redirect(url.full_url)



