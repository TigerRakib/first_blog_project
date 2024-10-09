from django.contrib import admin
from django.http import HttpRequest
from app1.models import GeneralInfo,our_services,testimonials,frequently_asked,contact_form_info,Blog,author
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display=[
        'company_name',
        'location'
    ]
@admin.register(our_services)
class our_servicesAdmin(admin.ModelAdmin):
    list_display=[
        'service_title'

    ]
    search_fields=[
        'service_title'
    ]
@admin.register(testimonials)
class testimonialsAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'title',
        'display_rating_count'
    ]
    def display_rating_count(self,obj):
        return "*" * obj.rating
    
@admin.register(frequently_asked)
class frequently_askedAdmin(admin.ModelAdmin):
    list_display=[
        'question'
    ]
@admin.register(contact_form_info)
class contact_form_infoAdmin(admin.ModelAdmin):
    list_display=[
        "email",
        "is_error",
        "is_success",
        "action_time"
    ]
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request ,obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=[
        "author",
        "title",
        "category"
    ]
@admin.register(author)
class authorAdmin(admin.ModelAdmin):
    list_display=[
        "first_name",
        "country",
        "joined_at"
    ]