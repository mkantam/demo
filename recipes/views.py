from rest_framework import status
from rest_framework import generics
from rest_framework import filters

from .models import Recipe
from .serializers import RecipeSerializer

from django.core.paginator import Paginator

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]