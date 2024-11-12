from rest_framework import serializers
from .models import Subject, Unit

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description', 'sub_icon']

class UnitSerializer(serializers.ModelSerializer):
    # Ensure pdf_file is included as a writable field
    pdf_file = serializers.FileField(required=True)

    class Meta:
        model = Unit
        fields = ['id', 'unit_name', 'pdf_file', 'subject']
