# Generated by Django 4.0.1 on 2022-04-02 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
        ),
    ]
