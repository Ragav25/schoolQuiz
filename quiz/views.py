import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


# Create your views here.

def queryparam_vaild(param):
    return param != '' and param is not None


def home(request):
    # CATEGORY URL
    category_url = requests.get('https://opentdb.com/api_category.php').json()

    # print("&&*****&&", category_url['trivia_categories'])

    categories = []

    for cat in category_url['trivia_categories']:
        category = {
            'category_id': cat['id'],
            'category_name': cat['name']
        }

        categories.append(category)

    # QUIZ QUESTION URL
    url = 'https://opentdb.com/api.php?amount=10&category={q_category}&difficulty={q_difficulty}&type=multiple'

    quiz_questions = []

    quiz_category = request.GET.get('quiz_category')
    quiz_difficulty = request.GET.get('quiz_difficulty')

    if queryparam_vaild(quiz_category) and queryparam_vaild(quiz_difficulty):
        r = requests.get(url.format(q_category=quiz_category,
                                    q_difficulty=quiz_difficulty)).json()

        for q in r['results']:
            questions = {
                'category': q['category'],
                'question': q['question'],
                'correct_answer': q['correct_answer'],
            }

            quiz_questions.append(questions)

    context = {
        'quiz_questions': quiz_questions,
        'categories': categories
    }

    return render(request, 'home.html', context)
