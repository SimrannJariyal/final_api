from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, UnitViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'units', UnitViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/subjects/<int:pk>/units/', UnitViewSet.as_view({'get': 'units_by_subject'}), name='subject-units'),
]
