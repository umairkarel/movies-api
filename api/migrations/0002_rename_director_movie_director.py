# Generated by Django 3.2.7 on 2021-10-12 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Director',
            new_name='director',
        ),
    ]
