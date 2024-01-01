from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    #  author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=50)
    blog_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField("опубликован")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.blog_title


class Comment(models.Model):  # maybe I should write inheritance
    #  author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1000)
    votes = models.IntegerField(default=0)

    #  def __str(self):
    #      return self.comment_text
