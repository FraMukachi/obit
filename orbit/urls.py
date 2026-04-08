from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from profiles import views as profiles_views
from chat import views as chat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.landing_page, name='landing'),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', accounts_views.custom_logout, name='logout'),
    path('dashboard/', accounts_views.dashboard, name='dashboard'),
    path('profile/', profiles_views.profile_view, name='profile'),
    path('matches/', profiles_views.matches_view, name='matches'),
    path('chat/<int:user_id>/', chat_views.chat_view, name='chat'),
]
