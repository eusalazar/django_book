from django.contrib import admin
from django.urls import path, include  # nuevo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('accounts/', include('accounts.urls')), # new
    path('', include('blog.urls')), 

]
