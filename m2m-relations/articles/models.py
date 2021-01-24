from django.db import models


class Tags(models.Model):

    name = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tags, through='ArticleTags', through_fields=('article', 'tags', 'is_main'))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleTags(models.Model):

    article = models.ForeignKey(Article, related_name='articles', verbose_name='Статья', on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, related_name='tags', verbose_name='Тэг', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        ordering = ['-is_main', 'tags__name']

    def __str__(self):
        return f'{self.article}_{self.tags}'


