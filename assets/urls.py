from django.urls import path
from assets.admin import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

#Titles in admin
admin.site.site_header = 'UC Riverside HPCC Asset Tracker'
admin.site.site_title = 'HPCC Asset Tracker Admin Portal'
admin.site.index_title = 'Welcome to the admin portal!'
