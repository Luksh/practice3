# Generated by Django 3.2.9 on 2021-12-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.TextField()),
                ('post', models.CharField(max_length=250)),
                ('comment', models.TextField()),
            ],
        ),
    ]