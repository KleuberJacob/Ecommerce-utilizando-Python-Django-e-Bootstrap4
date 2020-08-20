# Generated by Django 2.2.4 on 2019-08-15 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfis'},
        ),
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]