# Generated by Django 2.2.7 on 2019-11-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
            ],
        ),
    ]