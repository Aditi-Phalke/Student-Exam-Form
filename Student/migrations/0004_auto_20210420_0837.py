# Generated by Django 3.1.7 on 2021-04-20 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20210420_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='usn',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
