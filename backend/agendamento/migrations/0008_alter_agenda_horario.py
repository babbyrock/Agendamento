# Generated by Django 4.0.3 on 2022-03-27 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0007_agenda_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='horario',
            field=models.ManyToManyField(blank=True, to='agendamento.horario'),
        ),
    ]
