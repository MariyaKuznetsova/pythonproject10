from django.db import models


class Record(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    contents = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="Изображение")
    is_publication = models.BooleanField(default=True)
    number_of_views = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
        ordering = ["title", "contents"]

    def __str__(self):
        return self.title
