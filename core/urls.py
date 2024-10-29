from tkinter.font import names

from django.urls import path
from .views import IndexView

urlpatterns = [
path('',IndexView.as_view(),name='index.html')
]