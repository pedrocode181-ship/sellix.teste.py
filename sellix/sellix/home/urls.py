from .views import index, principal
from django.urls import path

urlpatterns = [
    path('', index, name='login'),
    path('principal/', principal, name='pagina principal')
]

