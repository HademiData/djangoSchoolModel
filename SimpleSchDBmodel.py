from django.db import models


GENDER_CHOICES = (
("Male", "Male"),
("Female", "Female")
)

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    # Other fields related to the school

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    # Other fields related to the student

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    # Other fields related to the teacher

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # Other fields related to the course

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Other fields related to the enrollment

    def __str__(self):
        return f"{self.student} - {self.course}"
