# Generated by Django 3.2.7 on 2022-07-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ex_user',
            name='phone',
            field=models.IntegerField(default=1),
        ),
    ]