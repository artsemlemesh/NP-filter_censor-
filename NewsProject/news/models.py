from django.db import models
from django.urls import reverse


# Товар для нашей витрины
class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, # названия товаров не должны повторяться
    )
    description = models.TextField()
    publish_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        to='NewsCategory',
        on_delete=models.CASCADE,
        related_name='news',
    )


    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class NewsCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()

