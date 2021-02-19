import datetime

from django.db import models
from django.db.models import DateTimeField
from django.urls import reverse
from django.utils import timezone

from users.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    author: User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pub_date: DateTimeField = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse('polls:detail', args=[self.id])

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
