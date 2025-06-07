from django.contrib import admin
from django.urls import path, include
from core.views import signup_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Connects app-level URLs to the project
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
