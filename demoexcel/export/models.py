from django.db import models


class Student(models.Model):
    name = models.CharField(default='', max_length=50)
    school = models.CharField(default='', max_length=25)
    grade = models.IntegerField()

    def __str__(self):
        return self.name
