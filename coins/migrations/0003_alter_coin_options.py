# Generated by Django 3.2 on 2021-04-24 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_alter_coin_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coin',
            options={'ordering': ['-price']},
        ),
    ]