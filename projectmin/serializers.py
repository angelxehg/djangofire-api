from django.shortcuts import render
from rest_framework import serializers
from projectmin.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Project
        fields = ('id', 'title', 'color', 'owner')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'project', 'content', 'status')
