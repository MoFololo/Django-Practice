from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.template import loader
from django.utils import timezone
from .models import Choice, Question, Comment
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
class CommentView(generic.ListView):
    model=Comment
    template_name = 'polls/comment.html'
    
    def comment_list_view(request):
        comments = Comment.objects.all()
        context = {'comments': comments}
        return render(request, 'polls/comment.html', context)

class CommentPostView(generic.DetailView):
    model=Comment
    template_name = 'polls/postcom.html'
    

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_commentset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404r(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def get_queryset(self):
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def comment(request):
    latest_comment_list = Comment.object.order_by('-pub_date')[:5]
    context = {'latest_comment_list': latest_comment_list}
    return render(request, 'polls/comment.html', context)

def comment_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        comment = Comment(title_text=title,comment_text=text)
        comment.save()
    return render(request, 'polls/postcom.html')