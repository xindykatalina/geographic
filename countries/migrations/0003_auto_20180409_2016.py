# Generated by Django 2.0.1 on 2018-04-09 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20180409_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(choices=[('CO', 'colombia'), ('MX', 'mexico'), ('USA', 'Estados Unidos'), ('AR', 'argentina')], max_length=3),
        ),
    ]
