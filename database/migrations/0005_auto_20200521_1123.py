# Generated by Django 2.2.6 on 2020-05-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20200430_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pulsar',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='pulsar',
            name='Bsurf',
        ),
        migrations.RemoveField(
            model_name='pulsar',
            name='Dist',
        ),
        migrations.RemoveField(
            model_name='pulsar',
            name='Edot',
        ),
        migrations.RemoveField(
            model_name='pulsar',
            name='Name',
        ),
        migrations.AddField(
            model_name='pulsar',
            name='AGE',
            field=models.FloatField(help_text='Spin down age (yr)', null=True),
        ),
        migrations.AddField(
            model_name='pulsar',
            name='BSURF',
            field=models.FloatField(help_text='Surface magnetic flux density (Gauss)', null=True),
        ),
        migrations.AddField(
            model_name='pulsar',
            name='DIST',
            field=models.FloatField(help_text='Best estimate of the pulsar distance using the YMW16 DM-based distance as default (kpc)', null=True),
        ),
        migrations.AddField(
            model_name='pulsar',
            name='EDOT',
            field=models.FloatField(help_text='Spin down energy loss rate (ergs/s)', null=True),
        ),
        migrations.AddField(
            model_name='pulsar',
            name='NAME',
            field=models.CharField(help_text='Pulsar name.  The B name if exists, otherwise the J name.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='DM',
            field=models.FloatField(help_text='Dispersion measure (cm-3 pc)', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='DM1',
            field=models.FloatField(help_text='First time derivative of dispersion measure (cm-3 pc yr-1)', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='F0',
            field=models.DecimalField(decimal_places=30, help_text='Barycentric rotation frequency (Hz)', max_digits=36, null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='F1',
            field=models.FloatField(help_text='Time derivative of barycentric rotation frequency (s-2)', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='F2',
            field=models.FloatField(help_text='Second time derivative of barycentric rotation frequency (s-3)', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='F3',
            field=models.FloatField(help_text='Second time derivative of barycentric rotation frequency (s-4)', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='P0',
            field=models.DecimalField(decimal_places=30, help_text='Barycentric period of the pulsar (s)', max_digits=32, null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='P1',
            field=models.FloatField(help_text='Time derivative of barcycentric period (dimensionless)', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='RM',
            field=models.FloatField(help_text='Rotation measure (rad m-2)', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='S1400',
            field=models.FloatField(help_text='Mean flux density at 1400 MHz (mJy)', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='S2000',
            field=models.FloatField(help_text='Mean flux density at 2000 MHz (mJy)', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='S400',
            field=models.FloatField(help_text='Mean flux density at 400 MHz (mJy)', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='W10',
            field=models.FloatField(help_text='Width of pulse at 10% (ms).', null=True),
        ),
        migrations.AlterField(
            model_name='pulsar',
            name='W50',
            field=models.FloatField(help_text='Width of pulse at 50% of peak (ms).', null=True),
        ),
    ]
