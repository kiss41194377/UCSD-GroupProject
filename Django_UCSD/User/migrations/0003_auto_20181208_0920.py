# Generated by Django 2.1.4 on 2018-12-08 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20181208_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_request', to='User.User'),
        ),
        migrations.AlterField(
            model_name='request',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_request', to='User.User'),
        ),
    ]
