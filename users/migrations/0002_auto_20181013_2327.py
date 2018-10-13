# Generated by Django 2.0.6 on 2018-10-13 23:27

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('work_begin', models.DateField()),
                ('work_end', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=90)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('additional_info', models.TextField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=15, null=True)),
                ('street', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('location', models.ForeignKey(on_delete='SET_NULL', related_name='qualifications', to='users.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='additional_qualification',
            field=models.ManyToManyField(related_name='seekers', to='users.Qualification'),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='education',
            field=models.ManyToManyField(related_name='seekers', to='users.Education'),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='personal_qualities',
            field=models.ManyToManyField(related_name='seekers', to='users.Quality'),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='skills',
            field=models.ManyToManyField(related_name='seekers', to='users.Skill'),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='work_experience',
            field=models.ManyToManyField(related_name='seekers', to='users.Company'),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.ForeignKey(on_delete='SET_NULL', related_name='companies', to='users.Location'),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.ManyToManyField(related_name='users', to='users.Location'),
        ),
    ]
