# Generated by Django 4.0.3 on 2022-04-04 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0017_rename_especialidade_id_medico_especialidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medico',
            old_name='especialidade',
            new_name='especialidade_id',
        ),
    ]