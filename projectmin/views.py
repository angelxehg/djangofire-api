from django.shortcuts import render
from rest_framework import viewsets
from projectmin.models import Project, Task
from projectmin.permissions import IsOwner
from projectmin.serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(owner=user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(project__owner=user)
