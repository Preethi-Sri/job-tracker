from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    # Auth
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Job Applications
    path('applications/', views.JobApplicationListCreateView.as_view(), name='applications'),
    path('applications/<int:pk>/', views.JobApplicationDetailView.as_view(), name='application-detail'),

    # Dashboard & Export
    path('dashboard/', views.dashboard_stats, name='dashboard'),
    path('export/', views.export_csv, name='export'),
    path('auth/reset-password/', views.reset_password, name='reset_password'),

    path('reset-password/', TemplateView.as_view(template_name='jobs/reset_password.html'), name='reset_password'),
]