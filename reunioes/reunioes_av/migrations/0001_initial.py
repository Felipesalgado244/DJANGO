# Generated by Django 4.2.9 on 2024-01-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReuniaoAv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('titulo', models.CharField(max_length=20)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('local', models.CharField(max_length=100)),
                ('dia', models.DateField()),
                ('horario', models.TimeField()),
            ],
        ),
    ]