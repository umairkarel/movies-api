# Generated by Django 3.2.7 on 2021-10-13 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211013_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.FloatField(),
        ),
    ]