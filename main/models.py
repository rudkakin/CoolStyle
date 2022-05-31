from tabnanny import verbose
from django.db import models

# Create your models here.
class Clothes(models.Model):
    title = models.CharField('Название', max_length=20)
    size = models.CharField('Размер', max_length=10, null=True)
    sex = models.CharField('Пол', max_length=10)
    category = models.CharField('Категория', max_length=20, null=True)
    image = models.CharField('Картинка', max_length=250)
    composition = models.CharField('Состав', max_length=50)
    price = models.CharField('Стоимость', max_length=10)

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'

    def __str__(self):
        return self.title