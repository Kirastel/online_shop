# Generated by Django 3.2.9 on 2022-04-03 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_product_availability'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Product Image', 'verbose_name_plural': 'Product Images'},
        ),
        migrations.DeleteModel(
            name='Accessories',
        ),
    ]