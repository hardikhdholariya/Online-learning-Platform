# Generated by Django 2.2 on 2020-02-04 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200130_1638'),
        ('subjects', '0002_auto_20200130_1637'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exam',
            new_name='Question',
        ),
    ]
