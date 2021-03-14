from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #<int:contato_id>' como argumento para a views
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
    path('busca/', views.busca, name='busca'),
]