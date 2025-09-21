from django.db import models
from django.contrib.auth import get_user_model


from django.db import models
from apps.categories.models import Categories

User = get_user_model()


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    image = models.ImageField(upload_to="products", verbose_name="Фото продукта")
    amount = models.IntegerField(verbose_name="Сумма")
    description = models.TextField(verbose_name="Описание")
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True , blank=True, verbose_name="Категория", related_name="product_category")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
