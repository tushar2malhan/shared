# Generated by Django 3.2.4 on 2021-07-21 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mammal',
            name='gender',
            field=models.CharField(choices=[('Male', 'female')], max_length=100),
        ),
        migrations.AlterField(
            model_name='mammal',
            name='last_feed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
