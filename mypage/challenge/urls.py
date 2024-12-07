from django.urls import path

from . import views

urlpatterns = [
    path('api/opencv_ops/', views.OpencvView.as_view(), name='opencv-api'),
    path('api/code_generation/', views.CodeGenerationView.as_view(), name='code_generation-api'),
]