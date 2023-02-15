from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

def vote(request, quetion_id):
    question = get_object_or_404(Question, pk=quetion_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{'question':question, 'error_message':"You didn't select a choice",})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))