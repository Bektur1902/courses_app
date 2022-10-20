from django.urls import path

from .views import *

urlpatterns = [
    path('courses-list/', CourseListView.as_view()),
    path('courses-create/', CourseListView.as_view()),
    path('courses/<int:pk>/', CourseDetailView.as_view())
]