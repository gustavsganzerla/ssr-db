# Generated by Django 5.0.3 on 2025-01-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cssr',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sequence', models.CharField(max_length=200)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('motif', models.CharField(max_length=50)),
                ('complexity', models.IntegerField()),
                ('length', models.IntegerField()),
                ('gap', models.IntegerField()),
                ('component', models.CharField(max_length=50)),
                ('structure', models.CharField(max_length=50)),
                ('clade', models.IntegerField()),
                ('subclade', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Issr',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sequence', models.CharField(max_length=200)),
                ('standard', models.CharField(max_length=50)),
                ('motif', models.CharField(max_length=50)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('length', models.IntegerField()),
                ('match', models.IntegerField()),
                ('subsitution', models.IntegerField()),
                ('insertion', models.IntegerField()),
                ('deletion', models.IntegerField()),
                ('score', models.FloatField()),
                ('clade', models.IntegerField()),
                ('subclade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ssr',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sequence', models.CharField(max_length=200)),
                ('standard', models.CharField(max_length=50)),
                ('motif', models.CharField(max_length=50)),
                ('repeat', models.IntegerField()),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('length', models.IntegerField()),
                ('clade', models.IntegerField()),
                ('subclade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vntr',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sequence', models.CharField(max_length=200)),
                ('motif', models.CharField(max_length=50)),
                ('repeat', models.IntegerField()),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('length', models.IntegerField()),
                ('clade', models.IntegerField()),
                ('subclade', models.CharField(max_length=50)),
            ],
        ),
    ]
