
from .models import Question
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger,InvalidPage
from django.shortcuts import render_to_response



from django.http import HttpResponseRedirect



def index(request):
    latest_question_list = Question.objects.all()
    paginator = Paginator(latest_question_list,4)

    page = request.GET.get('page')

    try:
         latest_question_list = paginator.page(page)
    except PageNotAnInteger:
         latest_question_list = paginator.page(1)
    except EmptyPage:
             latest_question_list = paginator.page(paginator.num_pages)
    return render_to_response("polls/index.html", {"latest_question_list": latest_question_list})



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

