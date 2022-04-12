from rest_framework import serializers

from apps.accounts.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
