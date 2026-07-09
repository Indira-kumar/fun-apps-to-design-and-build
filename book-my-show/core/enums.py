from django.db import models

class AuditoriumTypeEnum(models.TextChoices):
    TWO_D = "2D"
    THREE_D = "3D"
    FOUR_D = "4D"
    IMAX = "IMAX"
    SCREENX = "SCREENX"

class SeatTypeEnum(models.TextChoices):
    NORMAL = "NORMAL"
    COMFORTABLE = "COMFORTABLE"

class ShowSeatStatus(models.TextChoices):
    BOOKED = "booked"
    LOCKED = "locked"
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"

class PaymentStatusEnum(models.TextChoices):
    SUCCESS = "success"
    FAILED = "failed"
    PROCESSING = "processing"