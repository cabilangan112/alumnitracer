from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings

from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

# Create your models here.

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

CIVIL_STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Separated', 'Separated'),
    ('Widowed', 'Widowed')
)

class Index(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    cover_photo                         = models.ImageField(upload_to = 'media')
    title                               = models.CharField(max_length = 255)
    description                         = models.TextField()
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    @property
    def slug_title(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-id']

class Parallax(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    parallax_1                          = models.ImageField(upload_to='media')
    parallax_1_heading                  = models.CharField(max_length=255)
    parallax_1_content                  = models.TextField()
    parallax_2                          = models.ImageField(upload_to='media')
    parallax_2_heading                  = models.CharField(max_length=255)
    parallax_2_content                  = models.TextField()
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.parallax_1_heading)

    @property
    def slug_title(self):
        return '{}'.format(self.parallax_1_heading)

    class Meta:
        ordering = ['-id']

class Thumbnail(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    thumbnail                           = models.ImageField(upload_to='media')
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.user)

    @property
    def slug_title(self):
        return '{}'.format(self.user)

    class Meta:
        ordering = ['-id']

class Course(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    course_code                         = models.CharField(max_length = 255)
    course_description                  = models.TextField()
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.course_code, self.course_description)

    @property
    def slug_title(self):
        return '{}'.format(self.course_code)

    class Meta:
        ordering = ['-id']

class PersonalInformation(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    last_name                           = models.CharField(max_length = 255)
    first_name                          = models.CharField(max_length = 255)
    middle_name                         = models.CharField(max_length = 255)
    gender                              = models.CharField(
                                                            max_length = 6,
                                                            choices = GENDER
                                                        )
    date_of_birth                       = models.DateField()
    civil_status                        = models.CharField(
                                                        max_length = 10,
                                                        choices = CIVIL_STATUS
                                                    )
    age                                 = models.IntegerField()
    email                               = models.EmailField()
    mobile_number                       = models.CharField(max_length = 20)
    a_street_adress                     = models.TextField()
    a_address_line_2                    = models.TextField()
    a_city                              = models.CharField(max_length = 255)
    a_state_province_region             = models.CharField(max_length = 255)
    a_zip_code                          = models.CharField(max_length = 255)
    a_country                           = models.CharField(max_length = 255)
    b_street_adress                     = models.TextField()
    b_address_line_2                    = models.TextField()
    b_city                              = models.CharField(max_length = 255)
    b_state_province_region             = models.CharField(max_length = 255)
    b_zip_code                          = models.CharField(max_length = 255)
    b_country                           = models.CharField(max_length = 255)
    facebook_account                    = models.CharField(max_length = 255)
    twitter_account                     = models.CharField(max_length = 255)
    course                              = models.ForeignKey('Course', on_delete = models.CASCADE)
    date_graduated                      = models.DateTimeField()
    organization_or_employer            = models.CharField(max_length = 255)
    address_organization_or_employer    = models.CharField(max_length = 255)
    type_of_organization                = models.CharField(max_length = 20)
    employment_type                     = models.CharField(max_length = 60)
    occupational_classification         = models.CharField(max_length = 70)
    related_job                         = models.CharField(max_length = 3)
    number_year_company                 = models.CharField(max_length = 10)
    place_of_work                       = models.CharField(max_length = 6)
    finish_graduate_degree              = models.CharField(max_length = 3)
    reason_staying_job                  = models.TextField()
    designation                         = models.CharField(max_length = 255)
    department_division                 = models.CharField(max_length = 255)
    job_status                          = models.CharField(max_length = 11)
    monthly_range_income                = models.CharField(max_length = 255)
    persuing_degree_ndmc                = models.CharField(max_length = 3)
    obtaining_degree_ndmc               = models.TextField()
    current_job                         = models.CharField(max_length = 25)
    first_employment                    = models.TextField()
    work_related_course                 = models.CharField(max_length = 3)
    nature_of_employment                = models.CharField(max_length = 255)
    number_of_years                     = models.CharField(max_length = 10)
    monthly_income_range                = models.CharField(max_length = 20)
    reason_of_unemployed                = models.TextField()
    academic_professional               = models.CharField(max_length = 1)
    research_capability                 = models.CharField(max_length = 1)
    learning_efficiency                 = models.CharField(max_length = 1)
    communication_skills                = models.CharField(max_length = 1)
    people_skills                       = models.CharField(max_length = 1)
    problem_solving_skills              = models.CharField(max_length = 1)
    information_technology_skills       = models.CharField(max_length = 1)
    meeting_present                     = models.CharField(max_length = 1)
    local_community                     = models.CharField(max_length = 1)
    international_community             = models.CharField(max_length = 1)
    critical_thinking_skills            = models.CharField(max_length = 1)
    salary_improvement                  = models.CharField(max_length = 1)
    opportunities_abroad                = models.CharField(max_length = 1)
    personality_development             = models.CharField(max_length = 1)
    values_formation                    = models.CharField(max_length = 1)
    range_of_courses                    = models.CharField(max_length = 1)
    relevance_profession                = models.CharField(max_length = 1)
    extracurricular_activities          = models.CharField(max_length = 1)
    premium_given_research              = models.CharField(max_length = 1)
    interdisciplinary_learning          = models.CharField(max_length = 1)
    teaching_learning                   = models.CharField(max_length = 1)
    quality_instruction                 = models.CharField(max_length = 1)
    teacher_student_relationships       = models.CharField(max_length = 1)
    library_resources                   = models.CharField(max_length = 1)
    laboratory_resources                = models.CharField(max_length = 1)
    class_size                          = models.CharField(max_length = 1)
    professors_pedagogical              = models.CharField(max_length = 1)
    professors_knowledge                = models.CharField(max_length = 1)
    degree_program                      = models.CharField(max_length = 255)
    pursuing_further_studies            = models.CharField(max_length = 255)
    not_pursuing_further_studies        = models.CharField(max_length = 255)

    name_1                              = models.CharField(max_length = 255)
    contact_1                           = models.CharField(max_length = 255)
    email_id_1                          = models.CharField(max_length = 255)
    social_network_id_1                 = models.CharField(max_length = 255)

    name_2                              = models.CharField(max_length = 255)
    contact_2                           = models.CharField(max_length = 255)
    email_id_2                          = models.CharField(max_length = 255)
    social_network_id_2                 = models.CharField(max_length = 255)

    name_3                              = models.CharField(max_length = 255)
    contact_3                           = models.CharField(max_length = 255)
    email_id_3                          = models.CharField(max_length = 255)
    social_network_id_3                 = models.CharField(max_length = 255)

    name_4                              = models.CharField(max_length = 255)
    contact_4                           = models.CharField(max_length = 255)
    email_id_4                          = models.CharField(max_length = 255)
    social_network_id_4                 = models.CharField(max_length = 255)

    name_5                              = models.CharField(max_length = 255)
    contact_5                           = models.CharField(max_length = 255)
    email_id_5                          = models.CharField(max_length = 255)
    social_network_id_5                 = models.CharField(max_length = 255)



    
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}, {} {}'.format(
                        self.last_name,
                        self.first_name,
                        self.middle_name,
                        )

    @property
    def slug_title(self):
        return '{}'.format(self.last_name)

    class Meta:
        ordering = ['-id']

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Index)
pre_save.connect(rl_pre_save_receiver, sender=Thumbnail)
pre_save.connect(rl_pre_save_receiver, sender=Parallax)
pre_save.connect(rl_pre_save_receiver, sender=Course)
pre_save.connect(rl_pre_save_receiver, sender=PersonalInformation)