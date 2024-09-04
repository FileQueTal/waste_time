from .views import home, pagina, get_bike, get_by_nome, bike_manager
from django.urls import path

urlpatterns = [
    path('', home, name='index'),
    path('pagina/', pagina, name='pagina'),
    path('api/', get_bike, name='get_bike_api'),
    path('api/user/<str:nome>', get_by_nome, name='get_bike_nome_api'),
    path('api/data/', bike_manager, name='bike_manager_api')
]