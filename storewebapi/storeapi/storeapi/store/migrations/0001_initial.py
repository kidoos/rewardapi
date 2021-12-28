# Generated by Django 4.0 on 2021-12-27 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('customer_name', models.CharField(max_length=100)),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('purchase_amount', models.CharField(max_length=20)),
                ('reward_points', models.IntegerField(max_length=20)),
            ],
        ),
    ]
