from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from .models import Project, Experience, Education, Language, Skill, Certificate
from .forms import ContactForm

def index(request):
    featured_projects = Project.objects.all()[:3]
    return render(request, 'index.html', {'featured_projects': featured_projects})

def about(request):
    skills = Skill.objects.all()
    return render(request, 'about.html', {'skills': skills})

def resume(request):
    experiences = Experience.objects.all().order_by('-start_date')
    education = Education.objects.all().order_by('-start_date')
    technical_skills = Skill.objects.exclude(category='soft')
    soft_skills = Skill.objects.filter(category='soft')
    languages = Language.objects.all()
    certificates = Certificate.objects.all().order_by('-issue_date')
    
    context = {
        'experiences': experiences,
        'education': education,
        'technical_skills': technical_skills,
        'soft_skills': soft_skills,
        'languages': languages,
        'certificates': certificates,
    }
    return render(request, 'resume.html', context)

def projects(request):
    projects = Project.objects.all().order_by('-date_created')
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to database
            contact_message = form.save()
            
            # Send email notification (optional - remove if you don't want emails)
            try:
                # Use your existing email or a default one
                recipient_email = getattr(settings, 'CONTACT_EMAIL', settings.DEFAULT_FROM_EMAIL)
                
                send_mail(
                    f"Portfolio Contact: {form.cleaned_data['subject']}",
                    f"""New message from your portfolio website:

From: {form.cleaned_data['name']} ({form.cleaned_data['email']})
Subject: {form.cleaned_data['subject']}

Message:
{form.cleaned_data['message']}

---
This message was sent from your portfolio contact form.
                    """,
                    settings.DEFAULT_FROM_EMAIL,
                    [recipient_email],
                    fail_silently=True,  # Set to True to avoid errors if email fails
                )
            except Exception as e:
                # Log the error but don't break the form submission
                print(f"Email sending failed: {e}")
            
            # Return JSON response for AJAX or regular redirect
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
            else:
                messages.success(request, 'Your message has been sent successfully! I will get back to you within 24 hours.')
                return redirect('contact')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})