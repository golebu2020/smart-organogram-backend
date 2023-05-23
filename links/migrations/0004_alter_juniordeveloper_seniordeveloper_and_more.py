# Generated by Django 4.2 on 2023-05-02 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_remove_director_seniormanager_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juniordeveloper',
            name='seniorDeveloper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='links.seniordeveloper'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='seniorManager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='links.seniormanager'),
        ),
        migrations.AlterField(
            model_name='seniordeveloper',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='links.manager'),
        ),
        migrations.AlterField(
            model_name='seniormanager',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='links.director'),
        ),
    ]