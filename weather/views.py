from django.shortcuts import render
from .models import WedQuery, WedHistQuery, WedApi
import requests
from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.contrib.auth import get_user_model
from weather.utils.exceptions import ResourceNotFoundException

User = get_user_model()


def get_weather(request, user_pk):
    # if 'name' in request.GET:        if 'city' in querystring

    # city = 'London'

    user = get_object(User, user_pk)

    api = WedApi(api_id=user.user_api_id)

    params = {
        'q': 'London,uk',
        'units': 'metric',
    }
    response = requests.request("GET", api.url, headers=api.headers, params=params)
    temp = response.txt['main']['temp']

    wed_query = WedQuery(
        user=user.name,
        city='London',
        temp=temp
    )

    wed_query.save()

    return render(request, 'weather/weather.html', {'data': temp})


def get_object(_model, pk):
    try:
        return _model.objects.get(pk=pk)
    except _model.DoesNotExist:
        raise ResourceNotFoundException
