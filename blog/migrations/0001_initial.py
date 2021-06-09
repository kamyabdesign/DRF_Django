# Generated by Django 3.2.4 on 2021-06-09 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان مقاله')),
                ('slug', models.SlugField(unique=True, verbose_name='اسلاگ')),
                ('content', models.TextField(verbose_name='محتوا')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت مقاله')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
        ),
    ]