# Generated by Django 5.1.2 on 2024-10-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni lni-cog', 'Engrenagem'), ('lni lni-stats-up', 'Gráfico'), ('lni lni-users', 'Usuários'), ('lni lni-layers', 'Design'), ('lni lni-mobile', 'Mobile'), ('lni lni-rocket', 'Foguete')], max_length=100, verbose_name='Icone'),
        ),
    ]
