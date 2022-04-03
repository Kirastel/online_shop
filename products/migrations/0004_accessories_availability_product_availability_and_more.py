# Generated by Django 4.0.1 on 2022-03-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_is_active_alter_accessories_for_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='availability',
            field=models.CharField(choices=[('In', 'In stock'), ('Out', 'Out stock')], default='In stock', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.CharField(choices=[('In', 'In stock'), ('Out', 'Out stock')], default='In stock', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('iPhone', 'iPhone'), ('iPad', 'iPad'), ('Mac', 'Mac'), ('Airpods', 'Airpods')], max_length=10),
        ),
    ]