from rest_framework import generics 
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer, StudentDetailsSerializer, CourseSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import (
    CustomUser, StudentDetailsModels, CourseDetailsModels
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


class RegisterView(generics.CreateAPIView): 
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,) 
    serializer_class = RegisterSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CheckSessionView(APIView):
    def get(self, request, *args, **kwargs):
        session_data = {
            'refresh_token': request.session.get('refresh_token'),
            'access_token': request.session.get('access_token'),
            'user_email': request.session.get('user_email'),
        }
        return Response(session_data)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user

        user_data = {
            "name": user.get_full_name(),
            "email": user.email,
            "mobile": user.mobile,
        }
        return Response(user_data)
    

#student details create, delete, update, read
class StudentCreateView(APIView): 
    permission_classes = [IsAuthenticated] 

    def get(self, request, pk=None):
        print(pk)
        try: 
            if pk:
                student = StudentDetailsModels.objects.get(student_Id=pk)
                serializer_all = StudentDetailsSerializer(student)
                return Response(serializer_all.data)
            else:
                student = StudentDetailsModels.objects.all()
                seralizer = StudentDetailsSerializer(student, many=True)
                return Response(seralizer.data)
        except StudentDetailsModels.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # serializer = StudentDetailsSerializer(student)
        
    def post(self, request): 
        serializer = StudentDetailsSerializer(data=request.data, partial = True) 
        print(serializer)
        if serializer.is_valid():
            user_email = self.request.data['student_Email']
            print(user_email)
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None): 
        print(request.data)      
        try: 
            student = StudentDetailsModels.objects.get(student_Id=pk)
            print(student) 
        except StudentDetailsModels.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND) 
        serializer = StudentDetailsSerializer(student, data=request.data, partial = True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):

        try: 
            student = StudentDetailsModels.objects.get(student_Id=pk)
            print(student) 
        except StudentDetailsModels.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND) 
        student.delete()
        return Response({"message":"deleted"})
    

#course details create, delete, update, read
class CourseCreateView(APIView): 
    permission_classes = [IsAuthenticated] 

    def get(self, request, pk=None):
        print(pk)
        try: 
            course = CourseDetailsModels.objects.get(course_Id=pk)
        except CourseDetailsModels.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def post(self, request): 
        serializer = CourseSerializer(data=request.data, partial = True) 
        print(serializer)
        if serializer.is_valid():
            # user_email = self.request.data['student_Email']
            # print(user_email)
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None): 
        print(request.data)      
        try: 
            student = CourseDetailsModels.objects.get(course_Id=pk)
            print(student) 
        except CourseDetailsModels.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND) 
        serializer = CourseSerializer(student, data=request.data, partial = True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):

        try: 
            student = CourseDetailsModels.objects.get(course_Id=pk)
            print(student) 
        except CourseDetailsModels.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND) 
        student.delete()
        return Response({"message":"deleted"})

    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        request.session.flush()
        return Response({"message": "logged out"})