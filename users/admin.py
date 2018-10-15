from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User, Resume, Qualification, Quality, Skill, Location, Education, Company
)


resume_models = (
    Resume, Qualification, Quality, Skill, Location, Education, Company
)

admin.site.register(User, UserAdmin)
admin.site.register(resume_models)
