"""superlist URL Configuration
"""

from django.contrib import admin
from django.urls import path
# Views
from lists.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
]
