from operator import index
from xml.etree.ElementInclude import include
from django.urls import path
from . views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
]