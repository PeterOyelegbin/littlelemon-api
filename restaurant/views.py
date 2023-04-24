from rest_framework import viewsets, permissions, throttling
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import *
from .serializers import *


# Create your views here.
class MenuView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]
    ordering_fields = ['price', 'featured']
    search_fields = ['name', 'category__title']

    # restrict access for create, edit, and delete to admin only
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(BookingView, self).dispatch(request, *args, **kwargs)
    
    @method_decorator(csrf_exempt)
    def create(self, request, *args, **kwargs):
        data = request.data
        time_checker = Booking.objects.filter(date=data['date']).filter(
            time=data['time']).exists()
        if time_checker==True:
            return Response({'Message': 'Time is unavailable for today'}, 400)
        else:
            return super().create(request, *args, **kwargs)
