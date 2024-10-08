# Generated by Django 5.0.7 on 2024-08-14 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clg_admin', '0003_alter_regulation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='facultyadmin',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clg_admin.department', unique=True),
        ),
        migrations.AlterField(
            model_name='facultyadmin',
            name='dpt_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clg_admin.faculty', unique=True),
        ),
    ]
