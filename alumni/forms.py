from django import forms
from django.contrib.auth import get_user_model
from .models import PersonalInformation
from django_countries.data import COUNTRIES
 
GENDER = (
    ('', '--- SELECT ---'),
    ('Male', 'Male'),
    ('Female', 'Female')
    )

CIVIL_STATUS = (
    ('', '--- SELECT ---'),
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Separated', 'Separated'),
    ('Widowed', 'Widowed')
    )

CHOICES = (
    ('', '--- SELECT ---'),
    ('Poorly', 'Poorly'),
    ('Fairly', 'Fairly'),
    ('Highly', 'Highly'),
    ('Very Highly', 'Very Highly')
    )
STATUS = (
    ('', '--- Job Status ---'),   
    ('Permanent', 'Permanent'),
    ('Contractual', 'Contractual'),
    ('Casual', 'Casual'),
    )

PLACE_WORK = (
    ('', '--- Place of Work ---'),
    ('Local', 'Local'),
    ('Abroad', 'Abroad'),
    )
ORGANIZATION = (
    ('', '--- Select Organization ---'),
    ('Private', 'Private'),
    ('Public ', 'Public'),
    ('NGO', 'NGO'),
    ('Non-Profit ', 'Non-Profit'),
    )
COURSE_RELATED= (
    ('', '--- Course is Related to your Job? ---'),
    ('Yes', 'Yes'),
    ('No ', 'No'),
 
    )

User = get_user_model()

class PersonalInformationForm(forms.Form):

    user                = forms.ModelChoiceField(queryset=User.objects.all())
    civil_status        = forms.ChoiceField(choices=CIVIL_STATUS)
    age              = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    date_of_birth    = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    mobile_number    = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Mobile/Phone Number *:'}))
    a_street_adress  = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Sreet Address *'}))
    a_address_line_2 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Barangay *'}))
    a_city           = forms.CharField(max_length=210,widget=forms.TextInput(attrs={'placeholder': 'Municipality * '}))
    a_state_province_region =  forms.CharField(max_length=210,widget=forms.TextInput(attrs={'placeholder': 'Province  *'}))
    a_zip_code       = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder': 'ZIP Code *'}))
    a_country        =  forms.ChoiceField(choices = sorted(COUNTRIES.items()))
    facebook_account =  forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Facebook Account*'}))
    twitter_account  =  forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Twitter Acount *'}))
    instagram_account  =  forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Instagram Acount *'}))    
    
    organization_or_employer =  forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Name of Organization/Employer * '}))
    address_organization_or_employer =  forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Address of Organization/Employe * '}))
    type_of_organization        =  forms.ChoiceField(choices=ORGANIZATION )
    employment_type             =  forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Employment Type *'}))
 
    related_job                  = forms.ChoiceField(choices=COURSE_RELATED)
    number_year_company         = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Number of year in Company *'}))
    place_of_work               = forms.ChoiceField(choices=PLACE_WORK )
    finish_graduate_degree      = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Course Finished *'}))
    reason_staying_job          = forms.CharField(widget=forms.Textarea)
    designation                 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Designation *'}))
    department_division         = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Deparment Division *' }))
    job_status                  = forms.ChoiceField(choices=STATUS)
    monthly_range_income        = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Monthly Income Range *'}))
    persuing_degree_ndmc        = forms.ChoiceField(choices=COURSE_RELATED)
    obtaining_degree_ndmc       = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'If not, how long did it take you to find a job after obtaining your degree from NDMC? * '}))
    current_job                 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'How did you come to know about your current job? * '}))
    first_employment            = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'First Employment * '}))
    work_related_course         = forms.ChoiceField(choices=COURSE_RELATED)
    nature_of_employment        = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'IN THE CASE OF SELF EMPLOYMENT, what is the Nature of Employment? '}))
    number_of_years             = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Number Of Years Working on tharf Company *'}))
    monthly_income_range        = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Monthly Income Range *'}))
    degree_program              = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Degree Program * '}))
    pursuing_further_studies    = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'IF PURSUING FURTHER STUDIES *'}))
    not_pursuing_further_studies= forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'IF NOT PURSUING FURTHER STUDIES * '}))
    reason_of_unemployed        = forms.CharField(widget=forms.Textarea)

 

    def save(self):
        data = self.cleaned_data

        personal = PersonalInformation (
            user = data['user'],
            date_of_birth       = data['date_of_birth'],
            civil_status        = data['civil_status'],
            age                 = data['age'],

            mobile_number       = data['mobile_number'],
            a_street_adress     = data['a_street_adress'],                     
            a_address_line_2    = data['a_address_line_2'],                    
            a_city              = data['a_city'],                              
            a_state_province_region = data['a_state_province_region'],
            a_zip_code          = data['a_zip_code'],                          
            a_country           = data['a_country'],
            facebook_account    = data['facebook_account'],
            twitter_account     = data['twitter_account'],
            instagram_account     = data['instagram_account'],
            
            organization_or_employer = data['organization_or_employer'],
            address_organization_or_employer = data['address_organization_or_employer'],
            type_of_organization = data['type_of_organization'],
            employment_type      = data['employment_type'],
 
            related_job          = data['related_job'],
            number_year_company  = data['number_year_company'],
            place_of_work        = data['place_of_work'],
            finish_graduate_degree= data['finish_graduate_degree'],
            reason_staying_job = data['reason_staying_job'],
            designation          = data['designation'],
            department_division  = data['department_division'],
            job_status           = data['job_status'],
            monthly_range_income = data['monthly_range_income'],
            persuing_degree_ndmc = data['persuing_degree_ndmc'],
            obtaining_degree_ndmc= data['obtaining_degree_ndmc'],
            current_job          = data['current_job'],
            first_employment     = data['first_employment'],
            work_related_course  = data['work_related_course'],
            nature_of_employment = data['nature_of_employment'],
            number_of_years      = data['number_of_years'],
            monthly_income_range =  data['monthly_income_range'],               
            degree_program       = data['degree_program'],
            pursuing_further_studies = data['pursuing_further_studies'],     
            not_pursuing_further_studies = data['not_pursuing_further_studies'],
 
            )
        personal.save()



class PersonalEditForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = [
 
            'date_of_birth',
            'civil_status',
            'mobile_number',
            'a_street_adress',                     
            'a_address_line_2',                    
            'a_city',                              
            'a_state_province_region',
            'a_zip_code',                          
            'a_country',
            'facebook_account',
            'twitter_account',
            'instagram_account',
 
            'organization_or_employer',
            'address_organization_or_employer',
            'type_of_organization',
            'employment_type',

            'related_job',
            'number_year_company',
            'place_of_work',
            'finish_graduate_degree',
            'reason_staying_job',
            'designation',
            'department_division',
            'job_status',
            'monthly_range_income',
            'persuing_degree_ndmc',
            'obtaining_degree_ndmc',
            'current_job',
            'first_employment',
            'work_related_course',
            'nature_of_employment',
            'number_of_years',
            'monthly_income_range',               
            'reason_of_unemployed',
            'degree_program',
            'pursuing_further_studies',     
            'not_pursuing_further_studies',
        ]




