# Generated by Django 3.2.9 on 2021-11-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('severity', '0002_auto_20211114_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Age',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='Disease',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='Name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='Severity',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='Sex',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='Weight',
            field=models.CharField(default='', max_length=200),
        ),
    ]