# Generated by Django 4.0.1 on 2022-04-02 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_categories_alter_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
    ]