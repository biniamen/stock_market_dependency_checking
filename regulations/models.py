from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

User = get_user_model()

class Regulation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255)  # For storing dynamic regulation values
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_regulations')
    created_at = models.DateTimeField(default=now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.value}"


class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='audit_logs')
    timestamp = models.DateTimeField(default=now)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Action: {self.action} by {self.performed_by} at {self.timestamp}"


class StockSuspension(models.Model):
    SUSPENSION_TYPE_CHOICES = [
        ('Specific Stock', 'Specific Stock'),
        ('All Stocks', 'All Stocks'),
    ]
    INITIATOR_CHOICES = [
        ('Listing Company', 'Listing Company'),
        ('Regulatory Body', 'Regulatory Body'),
    ]

    trader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suspended_traders')
    stock = models.ForeignKey(
        'stocks.Stocks',  # Correctly reference the `Stocks` model
        on_delete=models.CASCADE,
        related_name='suspensions',
        null=True,
        blank=True  # Null if suspension applies to all stocks
    )
    suspension_type = models.CharField(max_length=20, choices=SUSPENSION_TYPE_CHOICES)
    initiator = models.CharField(max_length=20, choices=INITIATOR_CHOICES)
    reason = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    released_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.suspension_type == 'Specific Stock':
            return f"Suspension of {self.trader.username} for stock {self.stock.ticker_symbol}"
        return f"Suspension of all stocks owned by {self.trader.username}"


class WorkingHours(models.Model):
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day_of_week}: {self.start_time} - {self.end_time}"