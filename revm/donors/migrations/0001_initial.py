# Generated by Django 3.2.12 on 2022-02-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('contact_name', models.CharField(blank=True, max_length=255, verbose_name='contact name')),
                ('email', models.EmailField(max_length=255, verbose_name='email address')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, verbose_name='phone number')),
                ('type', models.SmallIntegerField(choices=[(1, 'Individual'), (2, 'Corporate'), (3, 'Non-Profit'), (4, 'Government')], default=1, verbose_name='type')),
                ('details', models.JSONField(blank=True, null=True, verbose_name='details')),
            ],
        ),
    ]
