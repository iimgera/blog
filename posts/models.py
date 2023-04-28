from django.db import models
from user.models import User


class Post(models.Model):
    title = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        verbose_name='Заголовок поста'
        ) 
    body = models.TextField(
        blank=True,
        null=True,
        verbose_name='Текст'
        )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name = 'Дата создания'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор'
        )
   
    def __str__(self):
        return self.title

    

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-id']