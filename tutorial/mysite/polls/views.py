from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

'''
Ideas for more tests¶
We ought to add a similar get_queryset method to ResultsView and create a new test class for that view. It’ll be very
 similar to what we have just created; in fact there will be a lot of repetition.

We could also improve our application in other ways, adding tests along the way. For example, it’s silly that Questions
 can be published on the site that have no Choices. So, our views could check for this, and exclude such Questions. 
 Our tests would create a Question without Choices and then test that it’s not published, as well as create a similar
 Question with Choices, and test that it is published.

Perhaps logged-in admin users should be allowed to see unpublished Questions, but not ordinary visitors. Again: whatever
 needs to be added to the software to accomplish this should be accompanied by a test, whether you write the test first
  and then make the code pass the test, or work out the logic in your code first and then write a test to prove it.

At a certain point you are bound to look at your tests and wonder whether your code is suffering from test bloat, which 
brings us to:



When testing, more is better¶
It might seem that our tests are growing out of control. At this rate there will soon be more code in our tests than in 
our application, and the repetition is unaesthetic, compared to the elegant conciseness of the rest of our code.

It doesn’t matter. Let them grow. For the most part, you can write a test once and then forget about it. It will 
continue performing its useful function as you continue to develop your program.

Sometimes tests will need to be updated. Suppose that we amend our views so that only Questions with Choices are 
published. In that case, many of our existing tests will fail - telling us exactly which tests need to be amended to 
bring them up to date, so to that extent tests help look after themselves.

At worst, as you continue developing, you might find that you have some tests that are now redundant. Even that’s not a 
problem; in testing redundancy is a good thing.

As long as your tests are sensibly arranged, they won’t become unmanageable. Good rules-of-thumb include having:

a separate TestClass for each model or view
a separate test method for each set of conditions you want to test
test method names that describe their function
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'  # would be called 'question_list' by default

    def get_queryset(self):
        '''
        Return the last five published questions (not including those set to be
        published in the future).
        '''
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
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
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))