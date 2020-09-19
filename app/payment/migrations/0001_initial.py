# Generated by Django 3.1.1 on 2020-09-18 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('is_time_extended', models.BooleanField(default=False)),
                ('extended_to_when', models.DateTimeField(null=True)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]