# Generated by Django 3.0.4 on 2022-08-26 17:30

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220826_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='json',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
