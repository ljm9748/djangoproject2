
from django.contrib import admin
from django.urls import path
import week6.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', week6.views.home, name="home"),
    path('submit/', week6.views.submit, name="submit"),
    
]