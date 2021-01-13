from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from extra_views import CreateWithInlinesView, InlineFormSetFactory

from .forms import QuestionForm, ChoiceForm
from .models import Choice, Question


def recent_polls(how_many=5):
    polls = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:how_many]
    return polls


class WithSidebar:
    def get_context_data(self, **kwargs):
        context = super(WithSidebar, self).get_context_data(**kwargs)
        context['recent_polls'] = recent_polls()
        return context


class ChoiceInline(InlineFormSetFactory):
    model = Choice
    form_class = ChoiceForm


class CreateQuestionView(WithSidebar, CreateWithInlinesView):
    model = Question
    inlines = (ChoiceInline,)
    form_class = QuestionForm
    template_name = 'polls/index.html'

    def forms_valid(self, form, inlines):
        form.instance.author = self.request.user
        return super(CreateQuestionView, self).forms_valid(form, inlines)


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
            'recent_polls': recent_polls(), # better: make this a class based view and inherit WithSidebar - need to
            # get that working tho
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return redirect(reverse('polls:results', args=(question.id,)))
