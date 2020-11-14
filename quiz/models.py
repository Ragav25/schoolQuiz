from django.db import models
from django.utils import timezone

# Create your models here.


class quizes(models.Model):
    quiz_name = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    category_id = models.TextField()
