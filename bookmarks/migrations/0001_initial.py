# Generated by Django 2.2 on 2019-04-24 04:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('is_public', models.BooleanField(default=True, verbose_name='Público?')),
                ('date_created', models.DateTimeField(verbose_name='Criado em')),
                ('date_updated', models.DateTimeField(verbose_name='Modificado em')),
                ('owner', models.ForeignKey(on_delete=True, related_name='bookmarks', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('tags', models.ManyToManyField(blank=True, to='bookmarks.Tag')),
            ],
            options={
                'verbose_name': 'bookmark',
                'verbose_name_plural': 'bookmarks',
                'ordering': ['-date_created'],
            },
        ),
    ]
