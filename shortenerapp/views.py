from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import URL

from .forms import URLForm

from django.db import IntegrityError
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def get_name(request):
    if request.method == 'POST':
        full_url = request.POST['full_url']
        url = URL(full_url=full_url)

        try:
            url.save()
        except IntegrityError:
            pass

        short_url = 'http://127.0.0.1:8000/' + url.url_hash
        context = {
            'form': URLForm(),
            'url_hash': short_url,
            'ur_link': 'Ваша ссылка: '
        }
        # testing if url is valid
        validate = URLValidator()
        try:
            validate(full_url)
        except ValidationError as e:
            context = {
                'form': URLForm(),
                'error': 'enter a valid url'
            }
            return render(request, 'shortenerapp/home.html', context=context)

        return render(request, 'shortenerapp/home.html', context=context)



        url = URL()
        url.save()
        # hash = url.save(full_url)
        # print(hash)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            return HttpResponse(full_url)

    # if a GET (or any other method) we'll create a blank form
    else:
        # if request.method == 'GET'
        form = URLForm()

    return render(request, 'shortenerapp/home.html', {'form': form})


def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    return redirect(url.full_url)



