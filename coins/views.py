from django.shortcuts import render

from .models import Pair


def index(request):
    new_pair = request.GET.get('new_pair')
    if new_pair:
        Pair.objects.get_or_create(name=new_pair)
    return render(request, "index.html")
