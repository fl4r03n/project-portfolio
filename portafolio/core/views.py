from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.

from about_me.models import (PortfolioHeader, AboutMe, FactDesc, Fact, Skill, SkillDesc, Education, Experience, ResumeDesc, PortfolioDesc, PortfolioItem, Service, ServicesDesc)


def home(request):
    portfolio_header = PortfolioHeader.objects.last()
    about_me = AboutMe.objects.last()
    facts_desc = FactDesc.objects.last()
    facts = Fact.objects.all()
    
    skills_desc = SkillDesc.objects.last()
    hard_skills = Skill.objects.filter(skill_type='hard')
    soft_skills = Skill.objects.filter(skill_type='soft')

    half_hard = (len(hard_skills) + 1) // 2
    left_hard_skills = hard_skills[:half_hard]
    right_hard_skills = hard_skills[half_hard:]

    half_soft = (len(soft_skills) + 1) // 2
    left_soft_skills = soft_skills[:half_soft]
    right_soft_skills = soft_skills[half_soft:]
    
    educations = Education.objects.all().order_by("-start_year")
    experiences = Experience.objects.all().order_by("-start_year")
    resume_desc = ResumeDesc.objects.last()

    for exp in experiences:
        if exp.responsibilities:
            exp.responsibilities_list = exp.responsibilities.split(",")

    items = PortfolioItem.objects.all().order_by('-project_date')
    portfolio_desc = PortfolioDesc.objects.last()
    
    services_desc = ServicesDesc.objects.last()
    services = Service.objects.all()
    
    return render(request,'core/home.html',
                  {"portfolio_header": portfolio_header,
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
                   "services": services,})
    
def portfolio_details(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    return render(request, "portfolio/portfolio-details.html", {"item": item})


def contact(request):
    return render(request,'core/contact.html')