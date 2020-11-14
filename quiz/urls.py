from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('online-quiz/<int:quiz_category>i<int:id>/<str:quiz_difficulty>',
         views.quiz_questions, name='quiz_questions_link')
]
