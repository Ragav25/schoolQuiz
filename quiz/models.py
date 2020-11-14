from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.


class Quizzes(models.Model):
    quiz_category = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    quiz_difficulty = models.CharField(
        max_length=100, default='easy', null=True, blank=True)

    def __str__(self):
        return self.quiz_category

    def get_absolute_url(self):
        return reverse("quiz_questions_link", kwargs={"quiz_category": self.quiz_category, "quiz_difficulty": self.quiz_difficulty,
                                                      "id": self.id})
        # f"online-quiz/{self.quiz_category}/{self.quiz_difficulty}"
