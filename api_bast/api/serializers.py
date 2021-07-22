from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['first_name', 'last_name',
                  'username', 'address', 'email', 'profile_image', ]
        model = Account
