# Generated by Django 5.1.4 on 2024-12-16 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_rename_project_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='service',
            name='subtitle',
            field=models.CharField(max_length=200, verbose_name='subtítulo'),
        ),
    ]
