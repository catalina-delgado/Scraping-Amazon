"""
URL configuration for scraper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import StartScraping, ShowProducts, StructureProducts

urlpatterns = [
    #mapeo,origen,referencia
    path('', StartScraping.as_view(), name='start_scraping'),
    path('start-scraping/', StartScraping.as_view(), name='start_scraping'),
    path('productos/', ShowProducts.as_view(), name='productos_lista'),
    path('estructurar/', StructureProducts.as_view(), name='estructurar'),
]

