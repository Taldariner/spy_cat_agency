# Generated by Django 4.2.16 on 2024-10-27 09:29

import cats.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpyCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('years_of_expirience', models.IntegerField(default=0)),
                ('breed', models.CharField(max_length=128, validators=[cats.validators.validate_breed])),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
    ]
