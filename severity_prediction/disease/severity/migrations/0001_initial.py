# Generated by Django 3.2.9 on 2021-11-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('Name', models.CharField(default='', max_length=50)),
                ('Sex', models.CharField(default='', max_length=15)),
                ('Age', models.IntegerField(default=0)),
                ('Weight', models.IntegerField(default=0)),
                ('Disease', models.CharField(default='', max_length=15)),
                ('Severity', models.CharField(default='', max_length=50)),
            ],
        ),
    ]