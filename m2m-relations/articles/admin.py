from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTags, Tags


class ArticleTagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags_count = 0

        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                main_tags_count += 1

        if main_tags_count > 1:
            raise ValidationError('Основной тэг может быть только один')

        elif main_tags_count == 0:
            raise ValidationError('Проставьте основной тэг')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleTagsInline(admin.TabularInline):
    model = ArticleTags
    formset = ArticleTagsInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagsInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass