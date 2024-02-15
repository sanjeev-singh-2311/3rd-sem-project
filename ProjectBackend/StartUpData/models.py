from django.db import models
from django.urls import reverse

# Create your models here.


class UserProjects(models.Model):
    username = models.CharField(max_length=100, verbose_name="User Name")
    projectID = models.CharField(
        primary_key=True, max_length=255, verbose_name="ProjectID")

    class Meta:
        verbose_name = "User Project"
        verbose_name_plural = "User Projects"

    def enterData(user, project):
        data = UserProjects()
        data.username = user
        data.projectID = project["ID"]

        data.save()

    def __str__(self):
        return f"{self.projectID} --> {self.username}"

    def get_absolute_url(self):
        return reverse("UserProjects_detail", kwargs={"pk": self.pk})
