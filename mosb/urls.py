from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

import mosb.core.views
from mosb.company.api.viewsets import CompanyViewSet
from mosb.training.api.viewsets import TrainingViewSet
from mosb.assessment.api.viewsets import AssessmentViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='Company')
router.register(r'trainings', TrainingViewSet, basename='Training')
router.register(r'assessments', AssessmentViewSet, basename='Assessments')


urlpatterns = [
    path('', mosb.core.views.home),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
