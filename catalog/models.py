from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категория")
    description = models.TextField(max_length=300, verbose_name="Описание категории")

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название продукта")
    description = models.CharField(max_length=150, verbose_name="Описание продукта")
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Категория продукта", related_name="products")
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "category", "price"]

    def __str__(self):
        return self.name



