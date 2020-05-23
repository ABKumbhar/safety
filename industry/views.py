from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import viewsets


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = industryserializers


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = equipmentserializers


class QnaiViewSet(viewsets.ModelViewSet):
    queryset = Qnai.objects.all()
    serializer_class = qnaiserializers


class QnaeViewSet(viewsets.ModelViewSet):
    queryset = Qnae.objects.all()
    serializer_class = qnaeserializers
