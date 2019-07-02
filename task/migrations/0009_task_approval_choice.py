# Generated by Django 2.0.5 on 2018-07-26 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20180726_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='approval_choice',
            field=models.CharField(choices=[(1, 'WAITING_FOR_VALIDATION'), (2, 'WAITING_FOR_IMPLEMENTATION'), (3, 'WAITING_FOR_APPROVAL'), (4, 'REFUSED'), (5, 'COMPLETED')], default=3, max_length=1),
        ),
    ]