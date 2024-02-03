from django.db import models


# Create Tag model
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    tag = models.ManyToManyField(Tag)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
