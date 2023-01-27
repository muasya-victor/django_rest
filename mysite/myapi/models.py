from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(TimestampMixin):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


