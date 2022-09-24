from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import ConferenceRoom, Reservation


class ConferenceRoomSerailizer(ModelSerializer):
    class Meta:
        model = ConferenceRoom
        fields = '__all__'


class ReservationSerializer(ModelSerializer):
    room = ConferenceRoomSerailizer
    class Meta:
        model = Reservation
        fields = ['id', 'room', 'date', 'start_time', 'end_time']

