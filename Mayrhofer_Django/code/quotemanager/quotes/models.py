from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.CharField(max_length=250)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text}"

