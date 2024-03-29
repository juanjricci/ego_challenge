# Generated by Django 4.2.11 on 2024-03-12 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('AUTO', 'Auto'), ('PICKUP', 'Pickup'), ('COMERCIAL', 'Comercial'), ('SUV', 'SUV'), ('CROSSOVER', 'Crossover')], default='AUTO', max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('anio', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=19)),
                ('thumbnail_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_url', models.URLField()),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('subtitulo', models.CharField(max_length=200)),
                ('descripcion_sub', models.TextField()),
                ('imagen_sub_url', models.URLField()),
                ('subtitulo_1', models.CharField(max_length=200)),
                ('descripcion_sub_1', models.TextField()),
                ('imagen_sub_1_url', models.URLField()),
                ('componentes', models.ManyToManyField(to='ego.componente')),
                ('modelo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ego.modelo')),
            ],
        ),
    ]
