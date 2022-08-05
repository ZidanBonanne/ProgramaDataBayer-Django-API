# Generated by Django 4.0.5 on 2022-07-04 15:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('ano_de_lancamento', models.IntegerField()),
                ('paginas', models.IntegerField()),
                ('editora', models.CharField(max_length=255)),
                ('disponivel', models.BooleanField()),
                ('descricao', models.TextField()),
                ('data_de_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
    ]