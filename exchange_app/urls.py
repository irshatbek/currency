from .views import exchange
from django.urls import path

urlpatterns = [
    path('', exchange),

]