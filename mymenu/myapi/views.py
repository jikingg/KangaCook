from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import MealPost
from .serializers import MealSerializer

class meals_list(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    queryset = MealPost.objects.all()
