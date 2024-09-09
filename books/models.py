from django.db import models
from authors.models import Authors


class Books(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name='books')
    isbn = models.IntegerField()
    category = models.CharField(max_length=50)
    publication_date = models.DateField(blank=True, null=True)
    is_borrowed = models.BooleanField(default=False)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return self.title, " from ", self.author
