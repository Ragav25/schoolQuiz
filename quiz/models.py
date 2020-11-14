from django.utils import timezone
from django.db import models

# Create your models here.


class Quizzes(models.Model):
    quiz_name = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    category_id = models.TextField()

    def __str__(self):
        return self.quiz_name
