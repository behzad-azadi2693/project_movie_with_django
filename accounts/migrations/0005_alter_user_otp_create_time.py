# Generated by Django 3.2.4 on 2021-09-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_movie_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp_create_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]