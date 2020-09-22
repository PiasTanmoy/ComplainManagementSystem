"""ComplainManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Student import views as student_view
from Complain import views as complain_view
from InfoNContact import views as info_contact_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('showTable/', student_view.showTables),
    path('studentForm/', student_view.studentForm),
    path('complainForm/', complain_view.complainForm),
    path('commentForm/', complain_view.commentForm),
    path('infoForm/', info_contact_view.infoForm),
    path('faqForm/',info_contact_view.faqForm)
]
