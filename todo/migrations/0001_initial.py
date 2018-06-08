# Generated by Django 2.0.6 on 2018-06-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, verbose_name='text')),
                ('done', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
            },
        ),
    ]
