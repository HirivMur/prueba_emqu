from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'encuestas'
urlpatterns = [
    #Catálogo de redes sociales
    path('redsocial/create/', RedSocialCreateView.as_view(),name='red-create'),
    path('redsocial/list/', RedSocialListView.as_view(),name='red-list'),
    path('redsocial/<pk>/update/', RedSocialUpdateView.as_view(),),

    path('create/', EncuestaCreateView.as_view(),name='encuesta-create'),
    path('estadisticas/list/', EstadisiticasListView.as_view(),name='estadistica-list'),
]