from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import TruncMonth
from .models import JobApplication
from .serializers import JobApplicationSerializer, RegisterSerializer, UserSerializer

# ── Auth Views ──
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# ── Job Application Views ──
class JobApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = JobApplication.objects.filter(user=self.request.user)
        status = self.request.query_params.get('status')
        search = self.request.query_params.get('search')
        if status and status != 'all':
            queryset = queryset.filter(status=status)
        if search:
            queryset = queryset.filter(company__icontains=search) | \
                      queryset.filter(role__icontains=search)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JobApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    user = request.user
    apps = JobApplication.objects.filter(user=user)

    stats = {
        'total': apps.count(),
        'applied': apps.filter(status='applied').count(),
        'interview': apps.filter(status='interview').count(),
        'offer': apps.filter(status='offer').count(),
        'rejected': apps.filter(status='rejected').count(),
    }

    # Monthly applications for chart
    monthly = apps.annotate(
        month=TruncMonth('applied_date')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')

    stats['monthly'] = [
        {
            'month': item['month'].strftime('%b %Y'),
            'count': item['count']
        }
        for item in monthly
    ]

    # By category chart
    by_status = apps.values('status').annotate(count=Count('id'))
    stats['by_status'] = list(by_status)

    return Response(stats)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_csv(request):
    import csv
    from django.http import HttpResponse

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="job_applications.csv"'

    writer = csv.writer(response)
    writer.writerow(['Company', 'Role', 'Location', 'Status', 'Type', 'Applied Date', 'Salary', 'Notes'])

    apps = JobApplication.objects.filter(user=request.user)
    for app in apps:
        writer.writerow([
            app.company, app.role, app.location,
            app.status, app.job_type, app.applied_date,
            app.salary, app.notes
        ])

    return response