from django.db import models
from .enums import AuditoriumTypeEnum, SeatTypeEnum, ShowSeatStatus, PaymentStatusEnum
from .base_model import BaseModel

class City(BaseModel):
    name = models.CharField(max_length=70)

class Theatre(BaseModel):
    name = models.CharField(max_length=70)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)

class Auditorium(BaseModel):
    name = models.CharField(max_length=20)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    auditorium_type = models.CharField(choices=AuditoriumTypeEnum.choices, max_length=30)

class Seat(BaseModel):
    number = models.IntegerField()
    position = models.JSONField()
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    seat_type = models.CharField(choices=SeatTypeEnum.choices, max_length=20)

class Movie(BaseModel):
    name = models.CharField(max_length=70)
    run_time = models.IntegerField()
    cast = models.JSONField()
    genre = models.CharField(max_length=70)
    certificate = models.CharField(max_length=20)

class Show(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    time = models.DateTimeField()

class User(BaseModel):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    city_preference = models.ForeignKey(City, on_delete=models.SET_NULL, null=True) # no way a city is removed, so no point in cascade delete, even if city is deleted
    contact = models.CharField(max_length=15)

class Booking(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE) 

class Payment(BaseModel):
    name = models.CharField(max_length=70)
    amount = models.FloatField() # could have paises, so float
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    status = models.CharField(choices=PaymentStatusEnum.choices, max_length=20)
    payment_method = models.CharField(max_length=20, choices=[('CARD', 'Card'), ('CASH', 'Cash'), ('UPI', 'UPI')])


class ShowSeat(BaseModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    status = models.CharField(choices=ShowSeatStatus.choices, default=ShowSeatStatus.AVAILABLE, max_length=20)
    booking = models.ForeignKey(Booking,on_delete=models.SET_NULL, related_name='show_seats', null=True, blank=True)
    cost = models.FloatField()
    
    class Meta:
        unique_together = ('show', 'seat')  # Each seat appears once per show