from django.contrib import admin
from django.urls import path
import mosb.core.views

urlpatterns = [
    path('', mosb.core.views.home),
    path('admin/', admin.site.urls),
]
