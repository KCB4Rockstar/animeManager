# Generated by Django 2.0.3 on 2018-03-31 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animeapp', '0006_auto_20180331_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='photoCover',
            field=models.ImageField(blank=True, null=True, upload_to='./animes/static/img/covers', verbose_name='cover photo'),
        ),
    ]
