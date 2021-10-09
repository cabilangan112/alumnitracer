from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.db.models import Q
from account.models import User
from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

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

CHOICES = (
    ('Poorly', 'Poorly'),
    ('Fairly', 'Fairly'),
    ('Highly', 'Highly'),
    ('Very Highly', 'Very Highly')
)

class PersonalQuerySet(models.query.QuerySet):
    def search(self,query): 
        if query:
            query = query.strip()
            return self.filter(
                Q(user__last_name__icontains=query)|
                Q(user__first_name__icontains=query)
                ).distinct()
        return self
 
class PersonalManager(models.Manager):
    def get_queryset(self):
        return PersonalQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)

class PersonalInformation(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    date_of_birth                       = models.CharField(max_length = 10)
    civil_status                        = models.CharField( max_length = 10, choices = CIVIL_STATUS)
    age                                 = models.CharField(max_length = 10)
    mobile_number                       = models.CharField(max_length = 20)
    a_street_adress                     = models.TextField()
    a_address_line_2                    = models.TextField()
    a_city                              = models.CharField(max_length = 255)
    a_state_province_region             = models.CharField(max_length = 255)
    a_zip_code                          = models.CharField(max_length = 255)
    a_country                           = models.CharField(max_length = 255)
    facebook_account                    = models.CharField(max_length = 255)
    twitter_account                     = models.CharField(max_length = 255)
    instagram_account                   = models.CharField(max_length = 255)    
 
    organization_or_employer            = models.CharField(max_length = 255)
    address_organization_or_employer    = models.CharField(max_length = 255)
    type_of_organization                = models.CharField(max_length = 20)
    employment_type                     = models.CharField(max_length = 60)
 
    related_job                         = models.CharField(max_length = 3)
    number_year_company                 = models.CharField(max_length = 10)
    place_of_work                       = models.CharField(max_length = 6)
    finish_graduate_degree              = models.CharField(max_length = 200)
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
    degree_program                      = models.CharField(max_length = 255)
    pursuing_further_studies            = models.CharField(max_length = 255)
    not_pursuing_further_studies        = models.CharField(max_length = 255)
    reason_of_unemployed                = models.TextField() 
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    objects = PersonalManager()

    def __str__(self):
        return '{}'.format(self.user.last_name)
 
    @property
    def slug_title(self):
        return '{}'.format(self.user.last_name)

    class Meta:
        ordering = ['-id']

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=PersonalInformation)