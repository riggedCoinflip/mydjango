from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
from .forms import QuestionForm, QuestionInlineFormSet

def recent_polls(how_many=5):
    polls = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:how_many]
    return polls


class WithSidebar:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WithSidebar, self).get_context_data(**kwargs)
        context['recent_polls'] = recent_polls()
        return context


class HomeView(WithSidebar, generic.CreateView):
    template_name = 'polls/home.html'
    model = Question
    form_class = QuestionForm
    success_url = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['question_form'] = QuestionForm(self.request.POST)
            context['choices_form_set'] = QuestionInlineFormSet(self.request.POST)
        else:
            context['question_form'] = QuestionForm()
            context['choices_form_set'] = QuestionInlineFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        choices = context['choices_form_set']
        if choices.is_valid() and form.is_valid():
            question_instance = form.save()
            for choice in choices:
                choice = choice.instance
                #get id of the newly created question.
                choice.question_id = question_instance.id
                choice.save()
            return HttpResponseRedirect(f'{question_instance.id}')
        else:
            return self.render_to_response(self.get_context_data(form=form))


class DetailView(WithSidebar, generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(WithSidebar, generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'recent_polls': recent_polls(), #better: make this a class based view and inherit WithSidebar - need to get that working tho
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

