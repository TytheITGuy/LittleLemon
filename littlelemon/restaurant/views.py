from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking
from .serializers import UserSerializer, MenuSerializer, BookingSerializer


# Template view for the homepage
def index(request):
    return render(request, 'index.html', {})


# DRF ViewSet for users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# Menu API views
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Booking API ViewSet
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

