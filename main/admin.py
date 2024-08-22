from django.contrib import admin
from .models import Group, Course, Student, GroupStudents, Lesson, Contract

admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(GroupStudents)
admin.site.register(Lesson)
admin.site.register(Contract)
