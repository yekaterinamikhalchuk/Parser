# Generated by Django 4.0.3 on 2022-05-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_alter_url_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
