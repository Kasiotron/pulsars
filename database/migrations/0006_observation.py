# Generated by Django 3.0.4 on 2020-06-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20200521_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateField(null=True)),
                ('frequency', models.FloatField(null=True)),
                ('length', models.FloatField(null=True)),
                ('pulses', models.IntegerField(null=True)),
            ],
        ),
    ]