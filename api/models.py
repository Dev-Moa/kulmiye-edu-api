from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

class EducationLanguage(models.Model):
    language_name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Education Languages"

    def __str__(self):
        return self.language_name

class EducationType(models.Model):
    type_name = models.CharField(max_length=150)

    def __str__(self):
        return self.type_name

class Degree(models.Model):
    degree_name = models.CharField(max_length=150)

    def __str__(self):
        return self.degree_name

    def get_absolute_url(self):
        return reverse("degree_detail", args=[self.id])

class Program(models.Model):
    program_name = models.CharField(max_length=150)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name="programs")
    year = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.program_name

    def get_absolute_url(self):
        return reverse("program_detail", args=[self.id])

class University(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='university')
    university_name = models.CharField(max_length=150)
    images = models.ImageField(upload_to='university', blank=True, null=True)
    programs = models.ManyToManyField(Program, related_name="universities")
    education_types = models.ManyToManyField(EducationType, related_name="universities")
    education_languages = models.ManyToManyField(EducationLanguage,related_name="universities")
    content = models.TextField(null=True)
    vision = models.TextField(null=True)
    mission = models.TextField(null=True)
    faculty_numbers = models.PositiveIntegerField(null=True)
    bachelor_program_numbers = models.PositiveIntegerField(null=True)
    master_program_numbers = models.PositiveIntegerField(null=True)
    phd_program_numbers = models.PositiveIntegerField(null=True)
    student_numbers = models.CharField(max_length=255, null=True)
    alumni_numbers = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True, null=True, allow_unicode=True)

    class Meta:
        verbose_name_plural = "Universities"
        ordering = ['university_name']

    def __str__(self):
        return self.university_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.university_name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("university_detail", args=[self.slug])

class ProgramScholarship(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="program_scholarships")
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="program_scholarships")
    scholarship_percentage = models.PositiveIntegerField(null=True)
    scholarship_year = models.PositiveIntegerField(null=True)

    class Meta:
        unique_together = (("program", "university"),)

    def __str__(self):
        return f"{self.program} at {self.university} ({self.scholarship_percentage}% scholarship)"

class Enrollment(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    student_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="enrollments")
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, related_name="enrollments")
    phone_number = models.CharField(max_length=20) 

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse("enrollment_detail", args=[self.id])
