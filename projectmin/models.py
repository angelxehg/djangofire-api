from django.db import models
from django.conf import settings


class Project(models.Model):

    COLORS = (
        ("primary", "primary"),
        ("secondary", "secondary"),
        ("success", "success"),
        ("danger", "danger"),
        ("warning", "warning"),
        ("info", "info"),
    )

    title = models.CharField(max_length=100)
    color = models.CharField(max_length=10, choices=COLORS, default="primary")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects'
    )


class Task(models.Model):

    STATUSES = (
        ("BACKLOG", "Backlog"),
        ("TODO", "To Do"),
        ("INPROGRESS", "In Progress"),
        ("REVIEW", "Review"),
        ("CLOSED", "Closed"),
    )

    content = models.CharField(max_length=200)
    status = models.CharField(
        max_length=10, choices=STATUSES, default="BACKLOG")

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
