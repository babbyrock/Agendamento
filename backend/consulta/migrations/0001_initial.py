# Generated by Django 4.0.3 on 2022-04-01 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamento', '0014_remove_medico_especialidade_medico_especialidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(max_length=30, null=True)),
                ('data_agendamento', models.DateTimeField(auto_now_add=True)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda_id', to='agendamento.agenda')),
                ('medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agenda_medico', to='agendamento.medico')),
            ],
        ),
    ]
