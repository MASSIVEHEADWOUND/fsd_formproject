from django.db import models

choices = (
    ('DG', 'Django'),
    ('FL', 'Flask'),
    ('PY', 'Python'),
    ('JS', 'JavaScript'),
)

class Project(models.Model):
    topic = models.CharField(max_length=100)
    duration = models.IntegerField()
    languages = models.CharField(max_length=100, choices = choices)

    def __str__(self):
        return self.topic