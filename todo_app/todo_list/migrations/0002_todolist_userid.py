# Generated by Django 3.0.4 on 2020-03-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='userid',
            field=models.IntegerField(default=1),
        ),
    ]
