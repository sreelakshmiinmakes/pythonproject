# Generated by Django 4.1.5 on 2023-04-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo2app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-4-7'),
            preserve_default=False,
        ),
    ]
