# Generated by Django 3.0.1 on 2020-03-03 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_teacher_image'),
        ('subjects', '0003_auto_20200209_1201'),
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Student'),
        ),
        migrations.AlterField(
            model_name='query',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject'),
        ),
    ]
