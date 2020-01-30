from django.shortcuts import render
from .models import sale
from rest_framework import viewsets
from social.myserializer import  socialSerializer
from social import  slp
from rest_framework.response import Response
from .models import sale
# Create your views here.
class  saleViewSet(viewsets.ModelViewSet):
    queryset =  sale.objects.order_by("-id")
    serializer_class = socialSerializer
    def create(self, request, *args, **kwargs):
        viewsets.ModelViewSet.create(self, request, *args, **kwargs)
        ob = sale.objects.latest("id")
        sal = slp.pred(ob)
        return Response({"Status":"success","sales": sal,'tmp':args})

