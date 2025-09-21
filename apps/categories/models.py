from django.db import models

# Create your models here.
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        verbose_name = "Катерогия"
        verbose_name_plural = "Категории"


    def __str__(self):
        return self.name
