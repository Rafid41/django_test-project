# Generated by Django 2.2.3 on 2022-05-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_orderlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacedOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Not given', max_length=20)),
                ('address', models.CharField(default='Not given', max_length=100)),
                ('phone_no', models.CharField(default='Not given', max_length=20)),
                ('products', models.CharField(default='0', max_length=200)),
            ],
        ),
    ]