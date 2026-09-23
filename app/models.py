from django.db import models


class Category(models.Model):
    # Название категории, unique=True - два одинаковых имени нельзя
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        # Как запись показывается в админке
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    # ForeignKey - у цитаты одна категория
    # on_delete=CASCADE - если категорию удалили, цитаты тоже удалятся
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quotes')
    # ManyToMany - у цитаты может быть много тегов, и наоборот
    tags = models.ManyToManyField(Tag, blank=True, related_name='quotes')
    # Дата ставится сама при создании
    created_at = models.DateTimeField(auto_now_add=True)
