# Generated by Django 4.0.4 on 2022-09-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='glxs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=40)),
            ],
        ),
    ]