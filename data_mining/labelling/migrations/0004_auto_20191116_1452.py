# Generated by Django 2.1.5 on 2019-11-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0003_auto_20191116_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='label',
            name='resulf',
        ),
        migrations.AddField(
            model_name='label',
            name='result',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
