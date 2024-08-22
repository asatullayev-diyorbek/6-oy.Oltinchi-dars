from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('courses/', views.CoursesView.as_view(), name='courses'),
    path('groups/', views.GroupsView.as_view(), name='groups'),
    path('students/', views.StudentsView.as_view(), name='students'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
