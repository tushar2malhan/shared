# Generated by Django 3.2.4 on 2021-07-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('species', models.CharField(blank=True, max_length=100, null=True)),
                ('food', models.CharField(max_length=100, null=True)),
                ('last_feed', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('species', models.CharField(max_length=100, null=True)),
                ('food', models.CharField(max_length=100, null=True)),
                ('count', models.IntegerField()),
                ('last_feed', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mammal',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('species', models.CharField(blank=True, max_length=100, null=True)),
                ('food', models.CharField(blank=True, max_length=100, null=True)),
                ('last_feed', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'female')], max_length=100)),
            ],
        ),
    ]
