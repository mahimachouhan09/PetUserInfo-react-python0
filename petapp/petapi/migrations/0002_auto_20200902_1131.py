# Generated by Django 2.2.16 on 2020-09-02 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='pet_name',
            new_name='name',
        ),
    ]
