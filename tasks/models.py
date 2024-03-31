from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority_choices = [
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]
    priority = models.CharField(max_length=10, choices=priority_choices, default="Low")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
