from django.urls import path
from .views import (
    RegisterView, CustomTokenObtainPairView, LogoutView, CheckSessionView, 
    UserProfileView, StudentCreateView, CourseCreateView
    )
from rest_framework_simplejwt.views import ( 
    TokenObtainPairView, 
    TokenRefreshView, 
    )

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), 
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('protected/', CheckSessionView.as_view(), name='protected'),
    path('student/<int:pk>/', StudentCreateView.as_view(), name='student-detail'), 
    path('student/', StudentCreateView.as_view(), name='student-delete'),
    path('course/<str:pk>/', CourseCreateView.as_view(), name='course-detail'), 
    path('course/', CourseCreateView.as_view(), name='course'),
]