from django.contrib import admin
from django.urls import path, include
from library.views import ReportView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    
    path('api/library/', include('library.urls')),
    path('api/reports/', ReportView.as_view(), name='reports'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
