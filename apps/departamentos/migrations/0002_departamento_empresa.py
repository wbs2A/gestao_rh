# Generated by Django 2.2.5 on 2019-09-06 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa'),
        ),
    ]