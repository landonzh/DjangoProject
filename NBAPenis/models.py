from django.db import models

class FanUser(models.Model):
    name       = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"

class Comment(models.Model):
    name       = models.CharField(max_length=100)
    comment    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.comment[:20]}…"
