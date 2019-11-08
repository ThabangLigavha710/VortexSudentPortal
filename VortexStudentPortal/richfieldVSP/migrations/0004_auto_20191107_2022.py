# Generated by Django 2.2.7 on 2019-11-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('richfieldVSP', '0003_create_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_user',
            name='contact_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='create_user',
            name='course',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='create_user',
            name='current_year',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='create_user',
            name='email_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='create_user',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='create_user',
            name='gender',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='create_user',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='create_user',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='create_user',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
