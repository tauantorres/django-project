# Generated by Django 4.2.2 on 2023-07-02 23:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('thumb', models.ImageField(upload_to='thumb_filmes')),
                ('descricao', models.TextField(max_length=1000)),
                ('categoria', models.CharField(choices=[('ANALISE', 'Análise'), ('PROGRAMACAO', 'Programação'), ('APRESENTACAO', 'Apresentação'), ('OUTROS', 'Outros')], max_length=20)),
                ('visualizacao', models.IntegerField(default=0)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]