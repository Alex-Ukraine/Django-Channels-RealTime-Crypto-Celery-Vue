import json

from django.http import JsonResponse
from django.shortcuts import render

from .models import Pair


def index(request):
    new_pair = request.GET.get('new_pair')
    if new_pair:
        Pair.objects.get_or_create(name=new_pair)
    return render(request, "index.html")


def pair_post(request):
    new_pair = request.GET.get('new_pair')
    if new_pair:
        object_pair, created = Pair.objects.get_or_create(name=new_pair)
        if created:
            print(object_pair.name, ' thanx')
            return JsonResponse({'new_pair': object_pair.name}, status=201)
        else:
            print(object_pair.name, ' thanx')
            return JsonResponse({'message': f'{object_pair.name} is already in db'}, status=200)
    return JsonResponse({'message': 'empty field'}, status=200)
