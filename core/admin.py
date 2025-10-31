from django.contrib import admin
from .models import Project, Experience, Education, Skill, Language, Certificate, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('title', 'technologies')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'location', 'start_date', 'end_date', 'current')
    list_filter = ('current', 'start_date')
    search_fields = ('position', 'company', 'location')
    fieldsets = (
        (None, {
            'fields': ('company', 'location', 'position', 'start_date', 'end_date', 'current')
        }),
        ('Descriptions', {
            'fields': ('short_description', 'description'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'location', 'start_date', 'end_date', 'current')
    list_filter = ('current', 'start_date')
    search_fields = ('degree', 'institution', 'location')
    fieldsets = (
        (None, {
            'fields': ('institution', 'location', 'degree', 'field_of_study', 'start_date', 'end_date', 'current')
        }),
        ('Descriptions', {
            'fields': ('short_description', 'description'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('order',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'accent', 'reading_proficiency', 'writing_proficiency', 'speaking_proficiency', 'listening_proficiency')
    list_filter = ('reading_proficiency', 'writing_proficiency', 'speaking_proficiency', 'listening_proficiency')
    search_fields = ('name', 'accent', 'accents')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'flag', 'accent', 'accents')
        }),
        ('Proficiency Levels', {
            'fields': (
                'reading_proficiency', 
                'writing_proficiency', 
                'speaking_proficiency', 
                'listening_proficiency'
            ),
            'classes': ('collapse',)
        }),
        ('Media & Certificates', {
            'fields': ('audio_sample', 'certificate'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuing_organization', 'issue_date')
    list_filter = ('issue_date',)
    search_fields = ('name', 'issuing_organization')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp', 'read')
    list_filter = ('read', 'timestamp')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('timestamp',)