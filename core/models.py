from django.db import models

class Project(models.Model):
    PROJECT_TYPES = [
        ('data-analytics', 'Data Analytics'),
        ('web-development', 'Web Development'),
        ('python-gui', 'Python GUI'),
        ('machine-learning', 'Machine Learning'),
        ('coming-soon', 'Coming Soon'),
    ]
    
    PROJECT_STATUS = [
        ('completed', 'Completed'),
        ('in-progress', 'In Progress'),
        ('planning', 'Planning'),
        ('coming-soon', 'Coming Soon'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=200)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='web-development')
    status = models.CharField(max_length=20, choices=PROJECT_STATUS, default='completed')
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    date_created = models.DateField()
    expected_launch = models.DateField(null=True, blank=True, help_text="For coming soon projects")
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]

    class Meta:
        ordering = ['-date_created']

class Experience(models.Model):
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True, help_text="City, Country")
    position = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, null=True, blank=True, help_text="Short summary for card view (max 300 chars)")
    description = models.TextField(help_text="Full description for modal view")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True, help_text="City, Country")
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    short_description = models.CharField(max_length=300, null=True, blank=True, help_text="Short summary for card view")
    description = models.TextField(blank=True, help_text="Full description for modal view")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('programming', 'Programming Languages'),
        ('web', 'Web Technologies'),
        ('data', 'Data Analysis'),
        ('soft', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    icon = models.ImageField(upload_to='skills/')
    order = models.IntegerField(default=0, help_text="Order in which skills appear")
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class Language(models.Model):
    PROFICIENCY_LEVELS = [
        ('native', 'Native / Fluent'),
        ('professional', 'Professional'),
        ('advanced', 'Advanced'),
        ('intermediate', 'Intermediate'),
        ('basic', 'Basic'),
        ('beginner', 'Beginner'),
    ]
    
    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='language_flags/', blank=True, null=True)
    accent = models.CharField(max_length=100, blank=True, help_text="e.g., American English, British English")
    accents = models.TextField(blank=True, help_text="Comma-separated list of accents/variants")
    
    # Proficiency levels
    reading_proficiency = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS, default='intermediate')
    writing_proficiency = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS, default='intermediate')
    speaking_proficiency = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS, default='intermediate')
    listening_proficiency = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS, default='intermediate')
    
    # Audio and certificates
    audio_sample = models.FileField(upload_to='language_samples/', blank=True, null=True)
    certificate = models.FileField(upload_to='language_certificates/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.accent})"
    
    @property
    def reading_percentage(self):
        return self.proficiency_to_percentage(self.reading_proficiency)
    
    @property
    def writing_percentage(self):
        return self.proficiency_to_percentage(self.writing_proficiency)
    
    @property
    def speaking_percentage(self):
        return self.proficiency_to_percentage(self.speaking_proficiency)
    
    @property
    def listening_percentage(self):
        return self.proficiency_to_percentage(self.listening_proficiency)
    
    def proficiency_to_percentage(self, proficiency):
        proficiency_map = {
            'native': 100,
            'professional': 90,
            'advanced': 80,
            'intermediate': 65,
            'basic': 40,
            'beginner': 20
        }
        return proficiency_map.get(proficiency, 50)
    
    @property
    def accents_list(self):
        if self.accents:
            return [accent.strip() for accent in self.accents.split(',')]
        return []

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    description = models.TextField(blank=True, help_text="Details about the certification")
    credential_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name}: {self.subject}"