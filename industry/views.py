from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.views import FlatMultipleModelAPIView
from rest_framework.decorators import action
from rest_framework.response import Response



class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = industryserializers

    @action(detail=False, methods=['GET'])
    def trending(self, request):
        query = Industry.objects.filter(trending= True)
        serializer = industryserializers(query,many=True)
        
        return Response(serializer.data,status=200)
  


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = equipmentserializers

    @action(detail=False, methods=['GET'])
    def trending(self, request):
        query = Equipment.objects.filter(trending= True)
        serializer = equipmentserializers(query,many=True)
        
        return Response(serializer.data,status=200)
  

class QnaiViewSet(viewsets.ModelViewSet):
    queryset = Qnai.objects.all()
    serializer_class = qnaiserializers


class QnaeViewSet(viewsets.ModelViewSet):
    queryset = Qnae.objects.all()
    serializer_class = qnaeserializers


class ApiAllView(FlatMultipleModelAPIView):
    add_model_type = True

    querylist = [{'queryset' : Industry.objects.all(),
    'serializer_class' :  industryserializers 
    },
    {'queryset' : Equipment.objects.all(),
    'serializer_class' :  equipmentserializers 
    }
    
    ]

    filter_backends = (SearchFilter,)
    search_fields = ('$name',)
    #'$adinfo','$equipment__name','$equipment__adinfo',)