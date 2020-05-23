from rest_framework import serializers
from .models import *




class industryserializers(serializers.ModelSerializer):
    questioni = serializers.HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='qnai-detail'
    )

    class Meta:
        model = Industry
        fields = '__all__'

class equipmentserializers(serializers.ModelSerializer):
    questione = serializers.HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='qnae-detail'
    )
    class Meta:
        model = Equipment
        fields = '__all__'

class qnaiserializers(serializers.ModelSerializer):
    class Meta:
        model = Qnai
        fields = '__all__'


class qnaeserializers(serializers.ModelSerializer):
    class Meta:
        model = Qnae
        fields = '__all__'

