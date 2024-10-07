
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(bool=True)


    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    user = models.ForeignKey(on_delete=models.CASCADE)

    def __str__(self):
        return self.text