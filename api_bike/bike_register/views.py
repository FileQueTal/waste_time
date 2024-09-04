from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import pagina_form, index_form, index_form_put
from .models import Bike
from .serializers import BikeSerializer
from django.shortcuts import redirect

from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore

import json

def home(request):
    form = index_form(request.GET or None)
    form_put = index_form_put(request.POST or None)
    return render(request, 'index.html', {'form_index':form, 'form_index_put':form_put})

def pagina(request):
    form = pagina_form(request.POST or None)
    #if form.is_valid():
    #    form.save()
    #    return redirect(home)
    return render(request, 'pagina.html', {'form_pagina':form})

@api_view(['GET'])
def get_bike(request):
    if request.method == 'GET':
        bikes = Bike.objects.all()
        serializer = BikeSerializer(bikes, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nome(request, nome):
    try:
        bike_model = Bike.objects.get(pk=nome)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = BikeSerializer(bike_model)
        return Response(serializer.data)

@api_view(['GET','POST','PUT','DELETE'])
def bike_manager(request):
    if request.method == 'GET':
        try:
            if request.GET['nome']:
                bike_name = request.GET['nome']
                try:
                    bike = Bike.objects.get(pk=bike_name)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = BikeSerializer(bike)
                return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        new_bike = request.data
        serializer = BikeSerializer(data=new_bike)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        bike_name = request.data['nome']
        try:
            updated_bike = Bike.objects.get(pk=bike_name)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BikeSerializer(updated_bike, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)