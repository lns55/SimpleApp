from django.db import models


class Task(models.Model):
    title = models.CharField('Task Title', max_length=50)
    task = models.TextField('Task Body')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'My Tasks'
