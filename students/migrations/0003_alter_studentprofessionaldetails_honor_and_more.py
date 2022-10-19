# Generated by Django 4.0.6 on 2022-07-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_studentprofessionaldetails_honor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofessionaldetails',
            name='honor',
            field=models.CharField(choices=[('PH', 'Physics'), ('MA', 'Mathematics')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofessionaldetails',
            name='minor',
            field=models.CharField(choices=[('PH', 'Physics'), ('MA', 'Mathematics')], max_length=255, null=True),
        ),
    ]
