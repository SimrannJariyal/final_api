# views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Subject, Unit
from .serializers import SubjectSerializer, UnitSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    @action(detail=True, methods=['get'], url_path='units')
    def units_by_subject(self, request, pk=None):
        """
        Custom action to get units for a particular subject.
        The subject ID is passed as `pk` in the URL.
        """
        subject = Subject.objects.get(pk=pk)  # Get the subject by pk
        units = subject.units.all()  # Access related units
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)
