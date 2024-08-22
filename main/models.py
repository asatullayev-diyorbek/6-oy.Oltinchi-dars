from django.db import models

# 1. course 2.groups 3. lesson 4. student 5. contract 6. group_students

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="courses/", null=True, blank=True)

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.name


class Group(BaseModel):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Guruh"
        verbose_name_plural = "Guruhlar"

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    name = models.CharField(max_length=100)
    date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"

    def __str__(self):
        return self.name


class Student(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"

    def __str__(self):
        return self.first_name + " " + self.last_name


class GroupStudents(BaseModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_status = models.BooleanField(default=False)
    reg_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = "Guruh o'quvchisi"
        verbose_name_plural = "Guruh o'quvchilari"

    def __str__(self):
        return self.group.name + " o'quvchilari"


class Contract(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=100)
    add_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = "Shartnoma"
        verbose_name_plural = "Shartnomalar"

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name + " " + self.contract_number
