# Generated by Django 3.2.3 on 2023-02-10 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pastel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cubierta', models.CharField(default=None, max_length=20)),
                ('precio', models.FloatField(default=None)),
                ('sabor', models.CharField(default=None, max_length=40)),
                ('peso', models.FloatField(default=None)),
                ('pisos', models.IntegerField()),
                ('tipo', models.CharField(default=None, max_length=40)),
            ],
        ),
    ]
