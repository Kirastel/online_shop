# Generated by Django 4.0.1 on 2022-03-13 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('total_price', models.FloatField(default=0.0, null=True)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('company', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=20)),
                ('zip', models.PositiveIntegerField(blank=True)),
                ('city', models.CharField(max_length=40)),
                ('province', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(blank=True, default=None, max_length=100, null=True)),
                ('status', models.CharField(choices=[('no', 'in processed'), ('yes', 'order completed')], default='no', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order')),
            ],
        ),
    ]
