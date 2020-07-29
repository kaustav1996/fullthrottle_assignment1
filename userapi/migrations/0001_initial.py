# Generated by Django 3.0.8 on 2020-07-29 08:59

from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=20)),
                ('tz', timezone_field.fields.TimeZoneField(default='Asia/Kolkata')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapi.Member')),
            ],
        ),
    ]
