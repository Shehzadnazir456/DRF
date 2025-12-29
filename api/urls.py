from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),          # employees
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
    path('blogs/<int:pk>',views.BlogDetailView.as_view()),
    path('comments/<int:pk>',views.CommentDetailView.as_view()),

]
