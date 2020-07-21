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
    lookup_field = 'slug'
    @action(detail=False, methods=['GET'])
    def trending(self, request):
        query = Industry.objects.filter(trending= True)
        serializer = industryserializers(query,many=True)
        
        return Response(serializer.data,status=200)
  

    @action(detail=True, methods=['GET'])
    def question(self, request, slug):
        query = self.get_object()
        questioni = Qnai.objects.filter(industry=query)
        serializer = qnaiserializers(questioni,many=True)
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
    serializer_class = gateserializers

class GateViewSet(viewsets.ModelViewSet):
    queryset = Gate.objects.all().order_by('index')
    serializer_class = gateserializers
    lookup_field = "path"

    @action(detail=False, methods=['GET'])
    def trending(self, request):
        query = Gate.objects.filter(trending= True)
        serializer = gateserializers(query,many=True)
        
        return Response(serializer.data,status=200)



class ApiAllView(FlatMultipleModelAPIView):
    add_model_type = True

    querylist = [{'queryset' : Industry.objects.all(),
    'serializer_class' :  industryserializers 
    },
    {'queryset' : Equipment.objects.all(),
    'serializer_class' :  equipmentserializers 
    },
    {'queryset' : Gate.objects.all(),
    'serializer_class' :  gateserializers 
    }
    
    
    ]

    filter_backends = (SearchFilter,)
    search_fields = ('$name',)
