# Generated by Django 2.1.1 on 2018-09-25 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kickstarter_app', '0002_project_kickstarter_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='usd_goal_real',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='usd_pledged_real',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
