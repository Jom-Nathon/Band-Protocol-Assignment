# Generated by Django 5.1.3 on 2024-11-17 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='payloadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
        ),
    ]