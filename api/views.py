from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics,viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer,CommentSerializer
from employees.models import Employee

# List all employees or create new
# @api_view(['GET', 'POST'])
# def employee_list(request):
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Retrieve, update, or delete single employee
# @api_view(['GET', 'PUT', 'DELETE'])
# def employee_detail(request, pk):
#     try:
#         employee = Employee.objects.get(pk=pk)
#     except Employee.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class Employees(generics.ListCreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = "pk"


# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset,many=True)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self,request,pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def update(self,request,pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer = EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data,status=status.HTTP_200_OK)
        
#     def delete(self,request,pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# BLOGS
class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# COMMENTS
class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()   # ✅ FIXED
    serializer_class = CommentSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field ='pk'
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field ='pk'


from rest_framework import mixins, generics
from .serializers import EmployeeSerializer

class EmployeeList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

