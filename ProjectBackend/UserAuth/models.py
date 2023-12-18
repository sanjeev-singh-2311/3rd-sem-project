from django.db import models

# Create your models here.
class UserData(models.Model):

	username = models.CharField(max_length=50, verbose_name = "UserName")
	email = models.EmailField(max_length=254, verbose_name = "UserEmail")
	password = models.CharField( max_length=50, verbose_name = "UserPass")

	class Meta:
		verbose_name = "UserData"
		verbose_name_plural = "UserDatas"

	def __str__(self):
		return f"{self.username}	{self.email}"

	def get_absolute_url(self):
		return reverse("UserData_detail", kwargs={"pk": self.pk})
