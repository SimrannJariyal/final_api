from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    sub_icon = models.ImageField(upload_to='subject_icons/', null=True, blank=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    unit_name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='unit_pdfs/')
    subject = models.ForeignKey(Subject, related_name='units', on_delete=models.CASCADE)

    def __str__(self):
        return self.unit_name
