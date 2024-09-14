from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.

from about_me.models import (PortfolioHeader, AboutMe, FactDesc, Fact, Skill, SkillDesc, Education, Experience, ResumeDesc, PortfolioDesc, PortfolioItem, Service, ServicesDesc, Testimonial, TestimonialDesc, ContactInfo)
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse


def get_skills():
    skills_desc = SkillDesc.objects.last()
    hard_skills = Skill.objects.filter(skill_type='hard')
    soft_skills = Skill.objects.filter(skill_type='soft')

    half_hard = (len(hard_skills) + 1) // 2
    left_hard_skills = hard_skills[:half_hard]
    right_hard_skills = hard_skills[half_hard:]

    half_soft = (len(soft_skills) + 1) // 2
    left_soft_skills = soft_skills[:half_soft]
    right_soft_skills = soft_skills[half_soft:]

    return skills_desc, left_hard_skills, right_hard_skills, left_soft_skills, right_soft_skills


def get_education_experiences():
    educations = Education.objects.all().order_by("-start_year")
    experiences = Experience.objects.all().order_by("-start_year")
    
    for exp in experiences:
        if exp.responsibilities:
            exp.responsibilities_list = exp.responsibilities.split(",")
    
    resume_desc = ResumeDesc.objects.last()
    return educations, experiences, resume_desc


def home(request):
    portfolio_header = PortfolioHeader.objects.last()
    about_me = AboutMe.objects.last()
    facts_desc = FactDesc.objects.last()
    facts = Fact.objects.all()

    # Llamamos a las funciones auxiliares
    skills_desc, left_hard_skills, right_hard_skills, left_soft_skills, right_soft_skills = get_skills()
    educations, experiences, resume_desc = get_education_experiences()

    items = PortfolioItem.objects.all().order_by('-project_date')
    portfolio_desc = PortfolioDesc.objects.last()

    services_desc = ServicesDesc.objects.last()
    services = Service.objects.all()

    testimonials_desc = TestimonialDesc.objects.last()
    testimonials = Testimonial.objects.all()
    
    contact_info = ContactInfo.objects.last()
    form = ContactForm()

    return render(
        request, 'core/home.html',
        {
            "portfolio_header": portfolio_header,
            "about_me": about_me,
            "facts_desc": facts_desc,
            "facts": facts,
            "skills_desc": skills_desc,
            "left_hard_skills": left_hard_skills,
            "right_hard_skills": right_hard_skills,
            "left_soft_skills": left_soft_skills,
            "right_soft_skills": right_soft_skills,
            "educations": educations,
            "experiences": experiences,
            "resume_desc": resume_desc,
            "items": items,
            "portfolio_desc": portfolio_desc,
            "services_desc": services_desc,
            "services": services,
            "testimonials_desc": testimonials_desc,
            "testimonials": testimonials,
            "form": form,
            "contact_info": contact_info
        }
    )
    
def portfolio_details(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    return render(request, "portfolio/portfolio-details.html", {"item": item})


def contact(request):
    contact_info = ContactInfo.objects.last()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            to_send = contact_info.email

            try:
                send_mail(
                    subject,
                    f"Mensaje de {name} ({email}):\n\n{message}",
                    settings.DEFAULT_FROM_EMAIL,
                    [to_send],
                    fail_silently=False,
                )
                response = {"success": True}
            except Exception as e:
                response = {"success": False, "error": str(e)}

            return JsonResponse(response)

    return JsonResponse({"success": False, "error": "Invalid request"})