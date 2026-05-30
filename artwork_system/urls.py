
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users.views.auth_views import *

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('auth/login/',login_view,name="login"),
    path('auth/register/',register_view,name="register"),
    path('auth/logout/',logout_view,name="logout"),
    path('auth/reset/',send_OTP,name="send_OTP"),
    path('auth/reset/newpassword/',reset_OTP,name="resetotp"),
    path('auth/reset/setpassword/',add_new_password,name="newpass"),

    path('users/', include('users.urls')),
    path('core/', include('core.urls')),
    path('commissions/',include('commissions.urls')),
    path('payments/', include('payments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
