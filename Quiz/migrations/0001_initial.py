# Generated by Django 3.2.6 on 2021-08-23 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='Texto de la pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='ElegirRespuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es la Pregunta Correcta?')),
                ('texto', models.TextField(verbose_name='Texto de la Pregunta')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='Quiz.preguntas')),
            ],
        ),
    ]
