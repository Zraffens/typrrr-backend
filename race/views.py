from django.shortcuts import render
from .models import Race
from .serializers import RaceSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


class RaceListView(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

