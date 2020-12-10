# Generated by Django 3.0.8 on 2020-10-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim_rating', '0005_auto_20201018_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim_rate',
            name='similarity',
            field=models.FloatField(choices=[(-3, 'totally different'), (-2, 'almost different'), (-1, 'a little bit different'), (0, 'nutral'), (1, 'a little bit similar'), (2, 'almost similar'), (3, 'totally similar')]),
        ),
    ]
