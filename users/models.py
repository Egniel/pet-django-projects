from django.contrib.auth.models import AbstractUser
from django.db import models

NULL = {
    'null': True,
    'blank': True,
}


class Quality(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Qualification(models.Model):
    name = models.CharField(max_length=60)
    location = models.ForeignKey(
        'Location', on_delete='SET_NULL', related_name='qualifications')
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return (
            f'{self.name} {self.date_start} - {self.date_end} {self.location}')


class Company(models.Model):
    name = models.CharField(max_length=60)
    location = models.ForeignKey(
        'Location', on_delete='SET_NULL', related_name='companies')
    work_begin = models.DateField()
    work_end = models.DateField(**NULL)
    #  achievements

    def __str__(self):
        return f'{self.name}'


class Education(models.Model):
    institution_name = models.CharField(max_length=90)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f'{self.institution_name}'


class Location(models.Model):
    country = models.CharField(max_length=30, **NULL)
    city = models.CharField(max_length=30, **NULL)
    postal_code = models.CharField(max_length=15, **NULL)
    street = models.CharField(max_length=60, **NULL)


class User(AbstractUser):
    first_name = models.CharField(max_length=20, **NULL)
    last_name = models.CharField(max_length=20, **NULL)
    birth_date = models.DateField(**NULL)
    location = models.ManyToManyField('Location', related_name='users')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.pk})'


class JobSeeker(User):
    education = models.ManyToManyField(
        'Education', related_name='seekers')
    work_experience = models.ManyToManyField(
        'Company', related_name='seekers')
    skills = models.ManyToManyField(
        'Skill', related_name='seekers')
    personal_qualities = models.ManyToManyField(
        'Quality', related_name='seekers')
    additional_qualification = models.ManyToManyField(
        'Qualification', related_name='seekers')
    additional_info = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.pk})'


