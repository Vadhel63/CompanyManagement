# Generated by Django 4.2.10 on 2024-04-05 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_manger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]