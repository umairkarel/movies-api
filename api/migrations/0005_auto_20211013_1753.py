# Generated by Django 3.2.7 on 2021-10-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_movie_runtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='gross',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='meta_score',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='votes',
            field=models.BigIntegerField(null=True),
        ),
    ]
