# Generated by Django 4.1.1 on 2022-10-04 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('strangecars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['time_create', 'title'], 'verbose_name': 'Странная машина', 'verbose_name_plural': 'Странные машины'},
        ),
        migrations.AddField(
            model_name='cars',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]