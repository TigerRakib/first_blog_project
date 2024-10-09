from django.shortcuts import render,redirect
from app1.models import GeneralInfo,our_services,testimonials,frequently_asked,contact_form_info,Blog
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def index(request):
    generalinfo=GeneralInfo.objects.first()
    all_services=our_services.objects.all()
    testimonial=testimonials.objects.all()
    frequently_asks=frequently_asked.objects.all()
    blogs=Blog.objects.all().order_by("-created_at")[:3]
    default_value=""
    
    context={
        'company_name':getattr(generalinfo,"company_name",default_value),
        'location':getattr(generalinfo,"location",default_value),
        'email':getattr(generalinfo,"email",default_value),
        'phone':getattr(generalinfo,"phone",default_value),
        'open_hours':getattr(generalinfo,"open_hours",default_value),
        'facebook_url':getattr(generalinfo,"facebook_url",default_value),
        'video_url':getattr(generalinfo,"video_url",default_value),
        'linkedin_url':getattr(generalinfo,"linkedin_url",default_value),
        'instragram_url':getattr(generalinfo,"instragram_url",default_value),
        'twitter_url':getattr(generalinfo,"twitter_url",default_value),
        'all_services':all_services,
        "testimonials":testimonial,
        'frequently_ask':frequently_asks,
        "blogs":blogs
    }
    return render(request,'index.html',context)
def contact_form(request):
    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        context={
            "name":name,
            "email":email,
            "subject":subject,
            "message":message
        }
        html_template=render_to_string("email.html",context)
        is_error=False
        is_success=False
        error_message=""
        try:
            send_mail(
                subject=subject,
                message=None,
                html_message=html_template,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False
            )
        except Exception as e :
            is_error=True
            error_message=str(e)
            messages.error(request,"There is an error!!!")
        else:
            is_success=True
            messages.success(request,"Email is sent successfully.")
        contact_form_info.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            action_time=timezone.now(),
            is_error=is_error,
            is_success=is_success,
            error_message=error_message
        )
    return redirect("home")
def blog_details(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    recent_post=Blog.objects.all().exclude(id=blog_id).order_by('-created_at')[:2]
    context={
        "blog_image":blog.blog_image,
        "category":blog.category,
        "title":blog.title,
        "author":blog.author,
        "created_at":blog.created_at,
        "content":blog.content,
        'recent_post':recent_post
    }
    return  render(request,'blog_details.html',context)
def blogs(request):
    all_blogs=Blog.objects.all().order_by('-created_at')
    paginator=Paginator(all_blogs,3)
    page=request.GET.get('page')
    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    except EmptyPage:
        blogs=paginator.page(paginator.num_pages)
    context={
        'blogs':blogs
    }
    return render(request,'blog.html',context)