# Generated by Django 4.0.2 on 2022-02-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingmax',
            name='bench_press',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trainingmax',
            name='deadlift',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trainingmax',
            name='overhead_press',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trainingmax',
            name='squat',
            field=models.IntegerField(),
        ),
    ]
