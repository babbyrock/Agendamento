# Generated by Django 4.0.3 on 2022-03-26 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0005_remove_agenda_horario_remove_agenda_medico'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agendamento.medico'),
        ),
    ]