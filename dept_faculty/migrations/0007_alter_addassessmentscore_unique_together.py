# Generated by Django 5.0.7 on 2024-08-28 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clg_admin', '0012_alter_facultyroles_name'),
        ('dept_admin', '0005_alter_facultyallocation_options'),
        ('dept_faculty', '0006_alter_addassessmentscore_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='addassessmentscore',
            unique_together={('student', 'assessment', 'subject')},
        ),
    ]
