# Generated by Django 5.0.2 on 2024-02-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoteTaking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]