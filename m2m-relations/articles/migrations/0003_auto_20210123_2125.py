# Generated by Django 3.1.2 on 2021-01-23 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210123_2119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletags',
            options={'ordering': ['-is_main', 'tags__name']},
        ),
        migrations.RenameField(
            model_name='tags',
            old_name='title',
            new_name='name',
        ),
    ]
