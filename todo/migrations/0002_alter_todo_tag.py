# Generated by Django 5.0.1 on 2024-02-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="tag",
            field=models.ManyToManyField(related_name="tag", to="todo.tag"),
        ),
    ]
