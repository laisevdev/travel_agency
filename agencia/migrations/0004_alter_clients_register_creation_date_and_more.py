# Generated by Django 5.0.6 on 2024-05-25 03:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencia', '0003_rename_id_paciente_trip_agenda_id_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients_register',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 25, 3, 9, 14, 702679, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trip_agenda',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 25, 3, 9, 14, 702679, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trip_agenda',
            name='payment_methods',
            field=models.CharField(choices=[('pix', 'PIX'), ('boleto', 'BOLETO'), ('transferencia_bancaria', 'TRANSFERÊNCIA BANCÁRIA'), ('cartao_de_credito', 'CARTÃO DE CRÉDITO'), ('cartao_de_debito', 'CARTÃO DE DÉBITO'), ('bitcoin_ou_criptomoedas', 'BITCOIN OU CRIPTOMOEDAS')], max_length=30),
        ),
    ]