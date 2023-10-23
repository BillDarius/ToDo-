# Generated by Django 4.2.6 on 2023-10-20 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pen', 'pending'), ('wat', 'watched')], default=('pen', 'pending'), max_length=5)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]