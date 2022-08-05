from asyncio.base_subprocess import ReadSubprocessPipeProto
from re import S
from django.forms import FloatField, TimeField
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView, ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView, GenericAPIView
from rest_framework import status, authentication, permissions
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from encuestas.serializers import *
from django.shortcuts import render, redirect
from django.db.models import Avg, Count, Sum, F
from django.db.models import TimeField, DateTimeField

from datetime import datetime
# Create your views here.

class EncuestaCreateView(APIView):
    permission_classes=(permissions.AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'encuesta.html'

    def get(self, request):
        serializer=EncuestasSerializer
        redes = RedesSocialesCatalogo.objects.all()
        return Response({'serializer':serializer, 'redes':redes})

    def post(self, request):
        try:
            correo=request.POST.get('correo')
            edad= request.POST.get('edad')
            sexo = request.POST.get('sexo')
            fecha = datetime.now()
            encuesta = Encuesta(correo=correo,edad=edad,sexo=sexo,fecha=fecha)
            encuesta.save()
            redes=request.POST.getlist('redSocialId')
            tiempos = request.POST.getlist('tiempo')
            try:
                for red in redes:
                    posicion= redes.index(red)
                    favorita=0
                    if int(request.POST.get('isFavorita'))==int(red):
                        favorita= 1
                    pregunta = Pregunta(encuesta_id=encuesta.id,redSocial_id=red,isFavorita=favorita,tiempo=tiempos[posicion])
                    pregunta.save()
            except:
                return Response({"response" : "Error en creación de encuesta"}, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"response" : "Error en creación de encuesta"}, status = status.HTTP_400_BAD_REQUEST)

        return redirect('encuestas:estadistica-list')

def obtenerFavoritoEdad(red):
    rangos={
    "18-25 años": Pregunta.objects.filter(redSocial_id=red.id, isFavorita=1,encuesta__edad__range=[18,25]).count(),
    "26-36 años": Pregunta.objects.filter(redSocial_id=red.id, isFavorita=1,encuesta__edad__range=[26,36]).count(),
    "34-40 años": Pregunta.objects.filter(redSocial_id=red.id, isFavorita=1,encuesta__edad__range=[34,40]).count(),
    "40 + años": Pregunta.objects.filter(redSocial_id=red.id, isFavorita=1,encuesta__edad__gt=40).count(),
    }
    max=0
    favorito=None
    for rango in rangos:
        if int(rangos[rango])>max:
            favorito=rango
    
    return favorito


class EstadisiticasListView(APIView):
    permission_classes = [permissions.AllowAny,]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'estadisticas.html'
    def get(self, request):
        redes=[]
        countFavorita=0
        
        redFavorita=None
        countNoFavorita=0
        redNoFavorita=None
        for red in RedesSocialesCatalogo.objects.all():
            promedio=None
            average = Pregunta.objects.filter(redSocial_id=red.id).aggregate(tiempo_avg=(Avg('tiempo')))
            
            favorita= Pregunta.objects.filter(redSocial_id=red.id, isFavorita=1).count()
            if favorita>=countFavorita:
                countFavorita=favorita
                redFavorita=red.descripcion
            
            noFavorita= Pregunta.objects.filter(redSocial_id=red.id, isFavorita=0).count()
            if noFavorita>=countNoFavorita:
                countNoFavorita=noFavorita
                redNoFavorita=red.descripcion
            if average["tiempo_avg"] != None:
                promedio= round(average["tiempo_avg"],2)
            redes.append({
                "redSocial":red.descripcion,
                "promedio":promedio,
                "favorita":favorita,
                "noFavorita":noFavorita,
                "rangoFavorito":obtenerFavoritoEdad(red)
            })
       
        estadistica={
            "encuesta": Encuesta.objects.count(),
            "favorita": redFavorita,
            "noFavorita": redNoFavorita,
            "redes": redes 
        }
        return Response({'content': estadistica}, status = status.HTTP_200_OK)