from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar_mensagem/', views.enviar_mensagem, name='enviar_mensagem'),
]
