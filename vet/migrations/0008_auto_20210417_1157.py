# Generated by Django 3.1.7 on 2021-04-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0007_clinica_trabajores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinica',
            name='trabajores',
        ),
        migrations.AddField(
            model_name='customuser',
            name='clinicas',
            field=models.ManyToManyField(to='vet.Clinica'),
        ),
    ]
