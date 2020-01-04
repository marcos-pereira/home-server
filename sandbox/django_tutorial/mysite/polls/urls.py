from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_view1', views.test_view1, name='test_view1')
]