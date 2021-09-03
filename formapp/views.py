from django.http import request
from django.shortcuts import render
from .forms import ResumeDetails

# Create your views here.

def formfunction(request):

    if request.method == 'POST':
        fm = ResumeDetails(request.POST)
        if fm.is_valid():
            global name
            global email
            global phone
            global desired_position
            global company_name
            global job_portal_name
            global degree

            name = fm.cleaned_data['Name']
            email = fm.cleaned_data['Email']
            phone = fm.cleaned_data['phone']
            desired_position = fm.cleaned_data['desired_position']
            company_name = fm.cleaned_data['company_name']
            job_portal_name = fm.cleaned_data['job_portal_name']
            degree = fm.cleaned_data['degree']
            
            
            print("Name :", name)
            print("Email :", email)
    
    else:  #pehli bar mai post nahi get hi ke sath wo form show hota hai. or isliye above condition gets fail and it show us that "fm is refrenced before assigned"  
        fm = ResumeDetails()
        print("ye get request se aya hai")

    return render(request, 'core/form.html', {'form': fm})


def resumemakerfunction(request):
    details = {'name':name,'email':email,'phone':phone,'desired_position':desired_position,'company_name':company_name,'job_portal_name':job_portal_name,'degree':degree }
    
    return render(request,'core/Resume.html',details)
