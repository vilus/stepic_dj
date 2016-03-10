from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question, Answer

 
def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def head(request):
    qu_list = Question.objects.order_by('-added_ad')

    paginator = Paginator(qu_list, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {'questions': questions})


@require_GET
def popular(request):
    qu_list = Question.objects.order_by('-rating')

    paginator = Paginator(qu_list, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {'questions': questions})


@require_GET
def question(request, qu_id):
    qu = get_object_or_404(Question, pk=qu_id)
    answers = Answer.objects.filter(question=qu)
    return render_to_response('question.html', {'question': qu, 'answers': answers})
