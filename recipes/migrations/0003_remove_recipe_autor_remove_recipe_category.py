# Generated by Django 4.0.3 on 2022-03-15 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_preparation_time_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
    ]
