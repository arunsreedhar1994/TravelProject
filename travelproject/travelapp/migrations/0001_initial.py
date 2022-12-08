# Generated by Django 4.1.2 on 2022-11-07 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('imj', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
