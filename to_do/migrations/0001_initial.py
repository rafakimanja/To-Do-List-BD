# Generated by Django 5.0.1 on 2024-01-03 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realizado', models.BooleanField()),
                ('descricao', models.CharField(max_length=50)),
                ('data', models.DateTimeField()),
            ],
        ),
    ]
