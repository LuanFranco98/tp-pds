# Generated by Django 3.2.9 on 2021-11-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20211120_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoria',
            new_name='categorias',
        ),
        migrations.AddField(
            model_name='categoria',
            name='posts',
            field=models.ManyToManyField(blank=True, to='usuario.Post'),
        ),
    ]
