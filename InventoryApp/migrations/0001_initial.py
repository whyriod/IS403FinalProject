# Generated by Django 3.2.8 on 2021-12-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('codigo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=30)),
                ('unidad', models.CharField(max_length=30)),
                ('stock', models.IntegerField()),
                ('dolares', models.DecimalField(decimal_places=2, max_digits=8)),
                ('soles', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_del_stock', models.DecimalField(decimal_places=2, max_digits=9)),
                ('tipo_de_cambio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'inventory',
            },
        ),
    ]
