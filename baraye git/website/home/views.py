from django.shortcuts import render
from django.http import HttpResponse
from.models import Question
from.forms import QuestionForm

def question_create(request):
    if request.method == 'POST'
        question.save ()
        return redirect('question_detail',slug = question.slug)
def question_list(request):
    questions = Question.object.all()

def question_update(request , slug):
    return redirect ('question_detail', slug = question.slug)

def question_delete(request,slug)
def home(request):
    return render(request,'home/home.html')


def all_product(request):
    return render(request,'home/product.html')