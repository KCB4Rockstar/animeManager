# Generated by Django 2.0.3 on 2018-04-04 05:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('animeapp', '0009_auto_20180331_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
