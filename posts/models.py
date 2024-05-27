from django.db import models

# Create your models here.

# {% for post in object_list %}
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
