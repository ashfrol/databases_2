from django.shortcuts import render

from articles.models import Article, ArticleTags


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    context['articles'] = []

    for article in Article.objects.all().order_by(ordering):
        article_object = {'article': article}

        for tag in article.tags.all():
            if ArticleTags.objects.filter(article_id=article.id, tags_id=tag.id).first().is_main:
                article_object['main_tag_id'] = tag.id
                break

        context['articles'].append(article_object)
        print(context)

    return render(request, template, context)