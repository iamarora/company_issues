# Generated by Django 3.2.8 on 2021-10-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companies',
            options={'ordering': ['name'], 'verbose_name_plural': 'companies'},
        ),
        migrations.AlterField(
            model_name='companies',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]