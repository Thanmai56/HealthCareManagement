# Generated by Django 5.1.1 on 2024-12-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_medicalrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('diagnosis', models.TextField()),
                ('treatment', models.TextField()),
                ('record_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='MedicalRecord',
        ),
    ]