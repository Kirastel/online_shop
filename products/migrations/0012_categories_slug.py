# Generated by Django 4.0.1 on 2022-04-02 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(default=None, null=True, unique=True),
        ),
    ]
