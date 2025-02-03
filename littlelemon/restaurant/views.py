from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


# Create your views here.
def index(request):
    return render(request, 'index1.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer