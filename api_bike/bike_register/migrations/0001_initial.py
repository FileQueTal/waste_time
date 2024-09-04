# Generated by Django 5.1 on 2024-08-31 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('nome', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('modelo', models.CharField(default='', max_length=20)),
                ('quantidade', models.IntegerField(default=0)),
                ('color', models.CharField(choices=[('BL', 'BLUE'), ('RD', 'RED'), ('GR', 'GREEN'), ('BR', 'BROWN')], max_length=10)),
            ],
        ),
    ]