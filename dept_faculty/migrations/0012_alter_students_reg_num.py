# Generated by Django 5.0.7 on 2024-08-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_faculty', '0011_students_reg_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='reg_num',
            field=models.CharField(max_length=10),
        ),
    ]
