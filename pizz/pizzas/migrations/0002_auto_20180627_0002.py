# Generated by Django 2.0.6 on 2018-06-26 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='name',
        ),
        migrations.AddField(
            model_name='pizza',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]