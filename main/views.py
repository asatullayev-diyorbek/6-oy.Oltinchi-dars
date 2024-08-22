from pprint import pprint

from django.shortcuts import render
from django.views.generic import View
from . import models


class HomeView(View):
    def get(self, request):
        courses = models.Course.objects.all()

        context = {
            'title': 'Bosh sahifa',
            'courses': courses,
        }
        return render(request, 'index.html', context)


class AboutView(View):
    def get(self, request):
        context = {
            'title': 'Biz haqimizda',
            'page_title': 'Biz haqimizda',
        }
        return render(request, 'about.html', context)


class CoursesView(View):
    def get(self, request):
        courses = models.Course.objects.all()
        context = {
            'title': 'Kurslar',
            'page_title': 'Kurslar',
            'courses': courses,
        }
        return render(request, 'courses.html', context)


class GroupsView(View):
    def get(self, request):
        groups = models.Group.objects.all()
        context = {
            'title': 'Guruhlar',
            'page_title': 'Guruhlar',
            'groups': groups,
        }
        return render(request, 'group.html', context)


class StudentsView(View):
    def get(self, request):
        group_students = models.GroupStudents.objects.all()
        context = {
            'title': "O'quvchilar",
            'page_title': "O'quvchilar",
            'group_students': group_students,
        }
        return render(request, 'students.html', context)


class ContactView(View):
    def get(self, request):
        context = {
            'title': 'Contact',
            'page_title': 'Contact',
        }
        return render(request, 'contact.html', context)
