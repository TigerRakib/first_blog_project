from django.db import models
from django.utils import timezone
class GeneralInfo(models.Model):
    company_name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    open_hours=models.CharField(max_length=255,blank=True,null=True)
    video_url=models.URLField(blank=True,null=True)
    facebook_url=models.URLField(blank=True,null=True)
    twitter_url=models.URLField(blank=True,null=True)
    linkedin_url=models.URLField(blank=True,null=True)
    instragram_url=models.URLField(blank=True,null=True)
    def __str__(self) :
        return self.company_name
class our_services(models.Model):
    icon=models.CharField(max_length=255)
    service_title=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.service_title
class testimonials(models.Model):
    name=models.CharField(max_length=255)
    picture=models.CharField(max_length=255,blank=True,null=True)
    title=models.CharField(max_length=255)
    description=models.TextField()
    rating=models.IntegerField()

    def __str__(self):
        return self.name
class frequently_asked(models.Model):
    question=models.CharField(max_length=255)
    answer=models.TextField()

    def __str__(self):
        return self.question
class contact_form_info(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    action_time=models.DateTimeField()
    is_error=models.BooleanField(default=False)
    is_success=models.BooleanField(default=False)
    error_message=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.email
class author(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    country=models.CharField(max_length=100)
    joined_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.first_name
class Blog(models.Model):
    blog_image=models.CharField(max_length=255,blank=True,null=True)
    category=models.CharField(max_length=100,blank=True,null=True)
    title=models.CharField(max_length=255)
    author=models.ForeignKey(author,on_delete=models.PROTECT,blank=True,null=True)
    created_at=models.DateTimeField(default=timezone.now)
    content=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.title
