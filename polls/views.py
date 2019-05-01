from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("You are at polls")
def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)
def results(request, question_id):
    response = "You're looking at the result of question %s. "
    return HttpResponse(response % question_id)
def vote(request, question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id )