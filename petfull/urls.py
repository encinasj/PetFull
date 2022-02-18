from django.urls import path
from petfull.views import index

urlpatterns = [
    path('home/', index.as_view()),
]
