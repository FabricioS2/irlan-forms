# Generated by Django 5.1.4 on 2024-12-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='Distancia',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Distancia'),
        ),
    ]
