# Generated by Django 4.0.6 on 2022-07-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_alert_api', '0003_alert_crytocurrency'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='user',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
