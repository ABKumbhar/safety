from rest_framework import serializers
from .models import *

class qnaiserializers(serializers.ModelSerializer):
    class Meta:
        model = Qnai
        fields = '__all__'

class gateserializers(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = '__all__'

class qnaeserializers(serializers.ModelSerializer):
    class Meta:
        model = Qnae
        fields = '__all__'

class equipmentserializers(serializers.ModelSerializer):
    questione = qnaeserializers(many=True, read_only=True)
    class Meta:
        model = Equipment
        fields = '__all__'


class industryserializers(serializers.ModelSerializer):
    questioni = qnaiserializers(
    many=True, read_only=True
    )
    equipment = equipmentserializers(many=True,read_only=True)
    class Meta:
        model = Industry
        fields = '__all__'




