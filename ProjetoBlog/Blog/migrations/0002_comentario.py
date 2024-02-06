# Generated by Django 5.0.1 on 2024-02-01 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('conteudo', models.TextField()),
                ('likes', models.IntegerField()),
                ('publicado_em', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Blog.post')),
            ],
            options={
                'ordering': ['-publicado_em'],
            },
        ),
    ]
