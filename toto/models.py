from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datePublished = models.DateTimeField(default=datetime.now())
    question_slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.question_slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Answer(models.Model):
    title = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datePublished = models.DateTimeField(default=datetime.now())
    content = RichTextField()

    def __str__(self):
        if(len(self.content) > 10):
            return self.content[:10] + "..."
        else:
            return self.content
