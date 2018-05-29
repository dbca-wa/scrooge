# Generated by Django 2.0.4 on 2018-05-29 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recoup', '0010_auto_20180116_0836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='costcentre',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='bill',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recoup.Contract'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recoup.FinancialYear'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cost_items', to='recoup.Bill'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='service_pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cost_items', to='recoup.ServicePool'),
        ),
        migrations.AlterField(
            model_name='costcentre',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recoup.Division'),
        ),
        migrations.AlterField(
            model_name='endusercost',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recoup.EndUserService'),
        ),
        migrations.AlterField(
            model_name='itplatformcost',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recoup.Platform'),
        ),
        migrations.AlterField(
            model_name='itsystem',
            name='cost_centre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='recoup.CostCentre'),
        ),
        migrations.AlterField(
            model_name='itsystem',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recoup.Division'),
        ),
        migrations.AlterField(
            model_name='systemdependency',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recoup.Platform'),
        ),
        migrations.AlterField(
            model_name='systemdependency',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recoup.ITSystem'),
        ),
    ]
