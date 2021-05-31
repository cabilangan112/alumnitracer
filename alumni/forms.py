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
    date_graduated   = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
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
    obtaining_degree_ndmc       = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Obtaining  Degree in NDMC * '}))
    current_job                 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Current Job * '}))
    first_employment            = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'First Employment * '}))
    work_related_course         = forms.ChoiceField(choices=COURSE_RELATED)
    nature_of_employment        = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'IN THE CASE OF SELF EMPLOYMENT, what is the Nature of Employment? '}))
    number_of_years             = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Number Of Years Working on tharf Company *'}))
    monthly_income_range        = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Monthly Income Range *'}))
    degree_program              = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Degree Program * '}))
    pursuing_further_studies    = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'IF PURSUING FURTHER STUDIES *'}))
    not_pursuing_further_studies= forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'IF NOT PURSUING FURTHER STUDIES * '}))
    reason_of_unemployed        = forms.CharField(widget=forms.Textarea)

    academic_professional     = forms.ChoiceField(choices=CHOICES )
    research_capability       = forms.ChoiceField(choices=CHOICES )
    learning_efficiency       = forms.ChoiceField(choices=CHOICES )
    communication_skills      = forms.ChoiceField(choices=CHOICES )
    people_skills             = forms.ChoiceField(choices=CHOICES )
    problem_solving_skills    = forms.ChoiceField(choices=CHOICES )
    information_technology_skills = forms.ChoiceField(choices=CHOICES )
    meeting_present           = forms.ChoiceField(choices=CHOICES )
    local_community           = forms.ChoiceField(choices=CHOICES )
    international_community   = forms.ChoiceField(choices=CHOICES )
    critical_thinking_skills  = forms.ChoiceField(choices=CHOICES )
    salary_improvement        = forms.ChoiceField(choices=CHOICES )
    opportunities_abroad      = forms.ChoiceField(choices=CHOICES )
    personality_development   = forms.ChoiceField(choices=CHOICES )
    values_formation          = forms.ChoiceField(choices=CHOICES )
    range_of_courses          = forms.ChoiceField(choices=CHOICES )
    relevance_profession      = forms.ChoiceField(choices=CHOICES )
    extracurricular_activities= forms.ChoiceField(choices=CHOICES )
    premium_given_research    = forms.ChoiceField(choices=CHOICES )
    interdisciplinary_learning= forms.ChoiceField(choices=CHOICES ) 
    teaching_learning         = forms.ChoiceField(choices=CHOICES )
    quality_instruction       = forms.ChoiceField(choices=CHOICES )
    teacher_student_relationships = forms.ChoiceField(choices=CHOICES )
    library_resources             = forms.ChoiceField(choices=CHOICES )
    laboratory_resources          = forms.ChoiceField(choices=CHOICES )
    class_size                    = forms.ChoiceField(choices=CHOICES )
    professors_pedagogical        = forms.ChoiceField(choices=CHOICES )
    professors_knowledge          = forms.ChoiceField(choices=CHOICES )


    def save(self):
        data = self.cleaned_data

        personal = PersonalInformation (
            user = data['user'],
            date_of_birth       = data['date_of_birth'],
            civil_status        = data['civil_status'],

            mobile_number       = data['mobile_number'],
            a_street_adress     = data['a_street_adress'],                     
            a_address_line_2    = data['a_address_line_2'],                    
            a_city              = data['a_city'],                              
            a_state_province_region = data['a_state_province_region'],
            a_zip_code          = data['a_zip_code'],                          
            a_country           = data['a_country'],
            facebook_account    = data['facebook_account'],
            twitter_account     = data['twitter_account'],
            date_graduated      = data['date_graduated'],
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

            reason_of_unemployed = data['reason_of_unemployed'],
            academic_professional = data['academic_professional'],
            research_capability  = data['research_capability'],
            learning_efficiency  = data['learning_efficiency'],
            communication_skills = data['communication_skills'],
            people_skills        = data['people_skills'],
            problem_solving_skills = data['problem_solving_skills'],
            information_technology_skills = data['information_technology_skills'],
            meeting_present      = data['meeting_present'],
            local_community      = data['local_community'],
            international_community  = data['international_community'],
            critical_thinking_skills = data['critical_thinking_skills'],
            salary_improvement       = data['salary_improvement'],
            opportunities_abroad     = data['opportunities_abroad'],
            personality_development  = data['personality_development'],
            values_formation         = data['values_formation'],
            range_of_courses         = data['range_of_courses'],
            relevance_profession     = data['relevance_profession'],
            extracurricular_activities = data['extracurricular_activities'],
            premium_given_research     = data['premium_given_research'],
            interdisciplinary_learning = data['interdisciplinary_learning'],
            teaching_learning        = data['teaching_learning'],
            quality_instruction      = data['quality_instruction'],
            teacher_student_relationships = data['teacher_student_relationships'],
            library_resources        = data['library_resources'],
            laboratory_resources     = data['laboratory_resources'],
            class_size               = data['class_size'],
            professors_pedagogical   = data['professors_pedagogical'],
            professors_knowledge     = data['professors_knowledge'],
            )
        personal.save()