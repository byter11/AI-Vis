from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_algorithm, name='index'),
    path('<slug:option>', views.get_algorithm, name='index'),
    path('/result', views.result, name='result'),

]