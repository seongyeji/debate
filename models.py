from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Debate(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(blank=True)
    body = models.TextField()
    agree = models.ManyToManyField(User, related_name='agree_debate', blank=True)

    def __str__(self):
        return self.title
        

class Comment(models.Model):
    post = models.ForeignKey('job_debate.Debate', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
 
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text