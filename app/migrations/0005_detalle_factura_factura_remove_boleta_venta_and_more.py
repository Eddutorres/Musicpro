# Generated by Django 4.1.5 on 2023-02-02 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_factura',
            fields=[
                ('id_detalle', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='boleta',
            name='venta',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='boleta',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='id_venta',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='rut_bodeguero',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='rut_cliente',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='registrado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.AddField(
            model_name='cliente',
            name='ap_mater_cli',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='ap_pater_cli',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_cli',
            field=models.IntegerField(default='1', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='SKU',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Bodegero',
        ),
        migrations.DeleteModel(
            name='Boleta',
        ),
        migrations.DeleteModel(
            name='Entrega',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
        migrations.AddField(
            model_name='factura',
            name='id_cli',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.cliente'),
        ),
        migrations.AddField(
            model_name='detalle_factura',
            name='SKU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.producto'),
        ),
        migrations.AddField(
            model_name='detalle_factura',
            name='id_factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.factura'),
        ),
    ]
