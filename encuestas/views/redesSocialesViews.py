from http.client import OK
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework import status, authentication, permissions
from encuestas.serializers import *
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
# Create your views here.

class RedSocialCreateView(CreateAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = RedesSocialesCatalogoSerializer


class RedSocialListView(ListAPIView):
    queryset = RedesSocialesCatalogo.objects.all()
    permission_classes = [permissions.AllowAny,]
    serializer_class = RedesSocialesCatalogoSerializer
    

class RedSocialUpdateView(UpdateAPIView):
    queryset = RedesSocialesCatalogo.objects.filter()
    permission_classes=(permissions.AllowAny,)
    serializer_class = RedesSocialesCatalogoSerializer
    http_method_names = ['put']