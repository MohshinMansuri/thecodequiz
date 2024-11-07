from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_view, name='quiz_view'),
    path('quiz/', views.quiz, name='quiz'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('already-registered/', views.already_registered, name='already_registered'),
    path('result/', views.result, name='result'),
]
