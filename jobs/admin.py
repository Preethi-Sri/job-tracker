from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['company', 'role', 'status', 'applied_date', 'location', 'user']
    list_filter = ['status', 'job_type']
    search_fields = ['company', 'role']