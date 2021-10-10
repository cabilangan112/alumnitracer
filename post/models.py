from django.db import models
from django.conf import settings
from django.urls import reverse 
User = settings.AUTH_USER_MODEL
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

POST_STATUS = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden'),
)

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    banner_photo = models.ImageField(upload_to = 'post')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=POST_STATUS, blank=True, default='published')
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    def current_hit_count(self):
        return self.hit_count.hits

    def __str__(self):
        return '{}'.format(self.user)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True) 
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.text)
