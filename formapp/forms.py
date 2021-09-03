from django import forms

class ResumeDetails(forms.Form):
    Name = forms.CharField(max_length='20')
    Email = forms.EmailField()
    phone = forms.IntegerField()
    desired_position = forms.CharField(max_length='30')
    company_name = forms.CharField(max_length='30')
    job_portal_name = forms.CharField(max_length='30')
    degree = forms.CharField(max_length='30')
    
    