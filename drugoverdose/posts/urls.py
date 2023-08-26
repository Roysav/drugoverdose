from django.urls import path, include
from . import views


urlpatterns = [
    path('question/', views.AskQuestion.as_view(), name='ask'),
]
