from django.urls import path
from .views import *

urlpatterns = [
    path("t1", Template1.as_view()),
    path("t2", Template2.as_view())

]