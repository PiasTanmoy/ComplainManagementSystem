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
from Tag import views as tag_views
from InfoNContact import views as infocontac_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('showTable/', student_view.showTables, name='showTable'),
    path('studentForm/', student_view.studentForm, name='studentForm'),
    path('complainForm/', complain_view.complainForm, name='complainForm'),
    path('commentForm/', complain_view.commentForm, name='commentForm'),
    path('voteForm/', complain_view.voteForm, name='voteForm'),
    path('tagForm/', tag_views.insertTag, name='tagForm'),
    path('complainTagForm/', tag_views.insertComplainTag, name='complainTagForm'),
    path('infoForm/', infocontac_views.infoForm, name='infoForm'),
    path('faqForm/', infocontac_views.faqForm, name='faqForm')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)