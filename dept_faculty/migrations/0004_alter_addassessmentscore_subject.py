# Generated by Django 5.0.7 on 2024-08-22 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_admin', '0004_alter_subjectallocation_unique_together'),
        ('dept_faculty', '0003_alter_addassessmentscore_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addassessmentscore',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dept_admin.subjectallocation'),
        ),
    ]
