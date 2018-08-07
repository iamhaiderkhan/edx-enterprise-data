# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-02 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnterpriseEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise_id', models.CharField(max_length=32)),
                ('enterprise_name', models.CharField(max_length=255)),
                ('lms_user_id', models.PositiveIntegerField()),
                ('enterprise_user_id', models.PositiveIntegerField()),
                ('course_id', models.CharField(help_text='The course the learner is enrolled in.', max_length=255)),
                ('enrollment_created_timestamp', models.DateTimeField()),
                ('user_current_enrollment_mode', models.CharField(max_length=32)),
                ('consent_granted', models.BooleanField(default=False)),
                ('letter_grade', models.CharField(max_length=32, null=True)),
                ('has_passed', models.BooleanField(default=False)),
                ('passed_timestamp', models.DateTimeField(null=True)),
                ('enterprise_sso_user_id', models.CharField(max_length=255, null=True)),
                ('course_title', models.CharField(max_length=255, null=True)),
                ('course_start', models.DateTimeField(null=True)),
                ('course_end', models.DateTimeField(null=True)),
                ('course_pacing_type', models.CharField(max_length=32, null=True)),
                ('course_duration_weeks', models.CharField(max_length=32, null=True)),
                ('course_min_effort', models.PositiveIntegerField(null=True)),
                ('course_max_effort', models.PositiveIntegerField(null=True)),
                ('user_account_creation_date', models.DateTimeField(null=True)),
                ('user_email', models.CharField(max_length=255, null=True)),
                ('user_username', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'enterprise_enrollment',
                'verbose_name': 'Enterprise Enrollment',
                'verbose_name_plural': 'Enterprise Enrollments',
            },
        )
    ]
