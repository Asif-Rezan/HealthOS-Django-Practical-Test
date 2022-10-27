# Generated by Django 4.1.2 on 2022-10-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='password1',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='password2',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=15),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
