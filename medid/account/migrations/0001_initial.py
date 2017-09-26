# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 20:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhardoc', models.IntegerField()),
                ('license', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_number', models.IntegerField(default=0)),
                ('unique_number', models.CharField(default=0, max_length=20)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=4)),
                ('address', models.CharField(max_length=220)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('emergency_contact', models.IntegerField()),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialno', models.IntegerField()),
                ('date_of_prescription', models.CharField(default='', max_length=20)),
                ('doctors_name', models.CharField(default='', max_length=20)),
                ('identifier', models.IntegerField(default=0)),
                ('medicine_text', models.CharField(choices=[('paracetomal', 'crocin-advance'), ('paracetomal', 'dolo')], max_length=30)),
                ('dosage', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=0)),
                ('consumption', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(default='', max_length=20)),
                ('report_date', models.CharField(default='', max_length=20)),
                ('unique_number', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='account.Patient')),
            ],
        ),
    ]