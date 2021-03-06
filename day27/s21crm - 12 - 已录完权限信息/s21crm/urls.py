"""s21crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from crm.views import account
from crm.views import depart
from crm.views import user
from crm.views import course
from crm.views import school
from crm.views import classes
from crm.views import public
from crm.views import private
from crm.views import record

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', account.login, name='login'),
    url(r'^index/', account.index, name='index'),
    
    url(r'^depart/list/', depart.depart_list, name='depart_list'),
    url(r'^depart/add/', depart.depart_add, name='depart_add'),
    url(r'^depart/edit/(\d+)/', depart.depart_edit, name='depart_edit'),
    url(r'^depart/del/(\d+)/', depart.depart_del, name='depart_del'),
    
    url(r'^user/list/', user.user_list, name='user_list'),
    url(r'^user/add/', user.user_add, name='user_add'),
    url(r'^user/edit/(\d+)/', user.user_edit, name='user_edit'),
    url(r'^user/del/(\d+)/', user.user_del, name='user_del'),
    
    url(r'^course/list/', course.course_list, name='course_list'),
    url(r'^course/add/', course.course_add, name='course_add'),
    url(r'^course/edit/(\d+)/', course.course_edit, name='course_edit'),
    url(r'^course/del/(\d+)/', course.course_del, name='course_del'),
    
    url(r'^school/list/', school.school_list, name='school_list'),
    url(r'^school/add/', school.school_add, name='school_add'),
    url(r'^school/edit/(\d+)/', school.school_edit, name='school_edit'),
    url(r'^school/del/(\d+)/', school.school_del, name='school_del'),
    
    url(r'^classes/list/', classes.classes_list, name='classes_list'),
    url(r'^classes/add/', classes.classes_add, name='classes_add'),
    url(r'^classes/edit/(\d+)/', classes.classes_edit, name='classes_edit'),
    url(r'^classes/del/(\d+)/', classes.classes_del, name='classes_del'),
    
    url(r'^public/customer/list/', public.public_customer_list, name='public_customer_list'),
    url(r'^public/customer/add/', public.public_customer_add, name='public_customer_add'),
    url(r'^public/customer/edit/(\d+)/', public.public_customer_edit, name='public_customer_edit'),
    url(r'^public/customer/del/(\d+)/', public.public_customer_del, name='public_customer_del'),
    
    url(r'^private/customer/list/', private.private_customer_list, name='private_customer_list'),
    url(r'^private/customer/add/', private.private_customer_add, name='private_customer_add'),
    url(r'^private/customer/edit/(\d+)/', private.private_customer_edit, name='private_customer_edit'),
    
    url(r'^record/list/(\d+)/', record.record_list, name='record_list'),
    url(r'^record/add/(\d+)/', record.record_add, name='record_add'),

]
