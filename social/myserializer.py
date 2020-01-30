from rest_framework import serializers
from social.models import  sale

class socialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  sale
        exclude = ()
        fields = '__all__'

