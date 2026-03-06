from django.db import models


class Reservation(models.Model):
    customer_name = models.CharField(max_length=120)
    start_at = models.DateTimeField()
    staff_name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return f"{self.customer_name} ({self.start_at})"
