from rest_framework import serializers
from base.models import CustomUser,ParagraphItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email','dob','password']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model=ParagraphItem
        fields=['paragraph','words']