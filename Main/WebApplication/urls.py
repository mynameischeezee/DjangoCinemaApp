from django.urls import path
from .views import test_view
from .views import MovieUnitList
urlpatterns = [
    path('', test_view, name='index')
]
