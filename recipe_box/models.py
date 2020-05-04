from django.db import models
# from django.utils import timezone

class Author(models.Model):
    name = models.Model(max_length = 30)
    byline = models.Model(max_length = 30)

    def __str__(self):
        return self.name

class RecipeItems(models.Model):
    title = models.CharField(max_length = 30)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author}"