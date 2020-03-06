from django.contrib import admin
from django.urls import path
from django.urls import include
from profile import views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/signup/', views.signup, name='signup'),
    path('profile/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('profile/logout/', views.logout_view, name='logout'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('profile/', include('django.contrib.auth.urls')),
    path('', include('notes.urls'))
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
