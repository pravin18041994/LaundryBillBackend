# Generated by Django 3.1.4 on 2021-01-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('owner_name', models.CharField(max_length=30)),
                ('fcm_token', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
