# Generated by Django 3.0.6 on 2020-05-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_name', models.CharField(max_length=100)),
                ('max_amount', models.IntegerField()),
                ('current_amount', models.IntegerField()),
            ],
        ),
    ]