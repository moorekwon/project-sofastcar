# Generated by Django 3.1.1 on 2020-09-19 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='extended_to_when',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='is_time_extended',
        ),
        migrations.AlterField(
            model_name='payment',
            name='distance',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]