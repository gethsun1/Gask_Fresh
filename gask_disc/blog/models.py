#from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(
        auto_now_add=True)  # default=timezone.now
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts-detail', kwargs={'pk': self.pk})
