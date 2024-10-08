# Generated by Django 5.0.7 on 2024-08-22 20:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clg_admin', '0009_alter_facultyadmin_department_and_more'),
        ('dept_admin', '0004_alter_subjectallocation_unique_together'),
        ('dept_faculty', '0002_alter_students_batch'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='addassessmentscore',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='addassessmentscore',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dept_admin.subjectallocation'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='addassessmentscore',
            unique_together={('student', 'assessment', 'subject')},
        ),
    ]
