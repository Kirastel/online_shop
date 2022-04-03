# Generated by Django 4.0.1 on 2022-03-13 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('iPhone', 'iPhone'), ('iPad', 'iPad'), ('iMac', 'iMac')], max_length=10)),
                ('generation', models.CharField(default=None, max_length=10)),
                ('version', models.CharField(blank=True, max_length=10)),
                ('storage', models.CharField(blank=True, max_length=10)),
                ('color', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='photos/')),
                ('is_active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]