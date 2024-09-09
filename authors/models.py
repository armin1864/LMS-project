from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=300)
    bio = models.CharField(max_length=2000, null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
