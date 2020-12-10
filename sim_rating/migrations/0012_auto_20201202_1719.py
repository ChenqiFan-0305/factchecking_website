# Generated by Django 3.0.8 on 2020-12-02 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sim_rating', '0011_auto_20201121_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='source',
        ),
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sim_rating.Source'),
        ),
    ]