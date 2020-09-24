# Generated by Django 3.1.1 on 2020-09-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='head',
            field=models.CharField(default='Saad', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_edited',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='reason',
            field=models.TextField(blank=True),
        ),
    ]