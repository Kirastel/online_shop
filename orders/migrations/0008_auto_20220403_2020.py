# Generated by Django 3.2.9 on 2022-04-03 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_contact_rename_f_name_order_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Product in order', 'verbose_name_plural': 'Products on order'},
        ),
    ]
