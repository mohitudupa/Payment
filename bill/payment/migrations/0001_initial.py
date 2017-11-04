# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bsnl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField()),
                ('due_date', models.DateField()),
                ('bill', models.IntegerField()),
                ('consumption', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField()),
                ('due_date', models.DateField()),
                ('bill', models.IntegerField()),
                ('consumption', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Electricity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField()),
                ('due_date', models.DateField()),
                ('bill', models.IntegerField()),
                ('consumption', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField()),
                ('due_date', models.DateField()),
                ('bill', models.IntegerField()),
                ('consumption', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField()),
                ('due_date', models.DateField()),
                ('bill', models.IntegerField()),
                ('consumption', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Telecom1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField()),
                ('due_date', models.DateField()),
                ('bill', models.IntegerField()),
                ('consumption', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Telecom2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField()),
                ('due_date', models.DateField()),
                ('bill', models.IntegerField()),
                ('consumption', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=25)),
                ('last', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=25)),
                ('area', models.CharField(max_length=25)),
                ('zip', models.IntegerField()),
                ('bal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField()),
                ('due_date', models.DateField()),
                ('bill', models.IntegerField()),
                ('consumption', models.IntegerField()),
                ('status', models.IntegerField()),
                ('aadhar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.User')),
            ],
        ),
        migrations.AddField(
            model_name='telecom2',
            name='aadhar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.User'),
        ),
        migrations.AddField(
            model_name='telecom1',
            name='aadhar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.User'),
        ),
        migrations.AddField(
            model_name='paper',
            name='aadhar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.User'),
        ),
        migrations.AddField(
            model_name='gas',
            name='aadhar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.User'),
        ),
        migrations.AddField(
            model_name='electricity',
            name='aadhar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.User'),
        ),
        migrations.AddField(
            model_name='cable',
            name='aadhar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.User'),
        ),
        migrations.AddField(
            model_name='bsnl',
            name='aadhar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.User'),
        ),
    ]