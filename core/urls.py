from django.contrib import admin
from django.urls import path
from . import views
app_name = "core"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name="home" )
    ]