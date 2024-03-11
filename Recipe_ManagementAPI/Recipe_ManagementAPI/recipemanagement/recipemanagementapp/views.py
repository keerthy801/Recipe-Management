from django.db.models import Q
from rest_framework import generics, viewsets, status
from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Recipe, Review_or_Comment
from .serializers import RecipeSerializer, ReviewSerializer, UserSerializer


class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # permission_classes = [IsAuthenticated]


class RecipeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.filter()
    serializer_class = RecipeSerializer
    # permission_classes = [IsAuthenticated]

class RecipeSearchView(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if (query):
            recipe=Recipe.objects.filter(Q(title__icontains=query) | Q(meal_type__icontains=query))
            s=RecipeSerializer(recipe,many=True)
            return Response(s.data)


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review_or_Comment.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        recipe_id = self.kwargs.get('recipe_id')
        return Review_or_Comment.objects.filter(recipe_id=recipe_id)

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response(status= status.HTTP_200_OK)


