from django.db import models

class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    details = models.CharField(max_length=40)

    def __str__(self):
        return self.emp_name  # ✅ Return a string
