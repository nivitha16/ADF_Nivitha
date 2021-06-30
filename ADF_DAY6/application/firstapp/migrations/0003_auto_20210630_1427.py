# Generated by Django 3.2.4 on 2021-06-30 08:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20210629_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='response_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_id', models.IntegerField()),
                ('response', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 30, 8, 57, 20, 497527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request_info',
            name='req_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 30, 8, 57, 20, 616475, tzinfo=utc)),
        ),

    ]
