# Generated by Django 4.2.3 on 2023-08-07 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_lesson_5', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='photo',
            field=models.ImageField(default=1, max_length=128, upload_to='', verbose_name='изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
