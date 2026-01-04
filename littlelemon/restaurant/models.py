from django.db import models


class Booking(models.Model):
    # Django will create an auto-increment primary key by default,
    # but we’ll define it explicitly to match the schema.
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    class Meta:
        db_table = "Booking"  # makes the MySQL table name exactly "Booking"

    def __str__(self):
        return f"{self.Name} ({self.BookingDate})"


class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    class Meta:
        db_table = "Menu"  # makes the MySQL table name exactly "Menu"

    def __str__(self):
        return self.Title

# Create your models here.
