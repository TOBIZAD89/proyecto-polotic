# Generated by Django 3.2.4 on 2021-07-06 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRUEBAAPP', '0004_delete_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='destacado',
            field=models.BooleanField(default=False),
        ),
    ]
