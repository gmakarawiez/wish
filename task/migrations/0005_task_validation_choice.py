# Generated by Django 2.0.5 on 2018-06-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20180608_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='validation_choice',
            field=models.CharField(choices=[(1, 'WAITING_FOR_VALIDATION'), (2, 'WAITING_FOR_IMPLEMENTATION'), (3, 'WAITING_FOR_APPROVAL'), (4, 'REFUSED'), (5, 'COMPLETED')], default=4, max_length=1),
        ),
    ]
