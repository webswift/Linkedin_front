# Generated by Django 2.0.5 on 2018-05-12 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0013_campaign_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='active',
        ),
    ]
