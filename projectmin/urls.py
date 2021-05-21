from rest_framework import routers
from projectmin.views import ProjectViewSet, TaskViewSet

projectmin_router = routers.DefaultRouter()
projectmin_router.register(r'projects', ProjectViewSet)
projectmin_router.register(r'tasks', TaskViewSet)
