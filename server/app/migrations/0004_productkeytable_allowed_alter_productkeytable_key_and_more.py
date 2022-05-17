# Generated by Django 4.0.1 on 2022-05-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_productkeytable_used_alter_productkeytable_key_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productkeytable',
            name='allowed',
            field=models.BooleanField(default=False, verbose_name='Activate / Deactivate'),
        ),
        migrations.AlterField(
            model_name='productkeytable',
            name='key',
            field=models.CharField(default='27f6ea26-7b5d-4315-893a-89337adf04ee', max_length=100, verbose_name='Product Key'),
        ),
        migrations.AlterField(
            model_name='productkeytable',
            name='used',
            field=models.BooleanField(default=False, verbose_name='Already being used by another machine'),
        ),
    ]
