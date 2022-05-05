from django.contrib import admin
from django.urls import path
# imported views
import hello.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # configured the url
    path('',views.index, name="homepage")
]
