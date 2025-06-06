# Generated by Django 5.2 on 2025-04-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numEmp', models.IntegerField(unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('nombre_jours', models.IntegerField()),
                ('taux_journalier', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
