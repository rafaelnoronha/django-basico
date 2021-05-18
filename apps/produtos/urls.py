from django.urls import path
from .views import produtos, produto

app_name = 'produtos'

urlpatterns = [
    path('', produtos, name='lista_produtos'),
    path('produto/<int:id_produto>/', produto, name='produto'),
]
