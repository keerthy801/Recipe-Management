from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Recipe, Review_or_Comment


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review_or_Comment
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']

    def create(self, validated_data): #After Validation
        user=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        user.save()
        return user
