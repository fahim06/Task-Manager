from django.urls import path, include
from rest_framework import routers
from .views import TaskList, TaskDetailView, TaskCreate, TaskUpdate, TaskDelete, TaskViewSet, TaskDeleteAPI

router = routers.DefaultRouter()
router.register(r'', TaskViewSet)

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('create/', TaskCreate.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('api/ <int:pk>/delete/', TaskDeleteAPI.as_view(), name='task_delete_api'),
    path('api/', include(router.urls)),
]
