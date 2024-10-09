"# first_blog_project" 
This is my first project .
Assignment Problem Statement:
Part 1:
  1.This is a blog web page ,where a user can see blogs articles
  2.User can send message via email.
  3.Pagination on blog page (sorted by blogs creation)

Technologies Used:
  Python
  Django
  Bootstrap
  JavaScript
  SQL 
  HTML 
  CSS 
Additional Python Modules Required
 1.from django.core.mail import send_mail
 2.from django.conf import settings
 3.from django.template.loader import render_to_string
 4.from django.contrib import messages
 5.from django.utils import timezone
 6.from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
