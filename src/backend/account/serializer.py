from rest_framework import serializers
from .models import User, Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
                     'id', 'email', 'first_name', 'last_name', 'mobile', 'is_staff', 'is_active', 'is_superuser',
                 )


class CustomerSerializer(serializers.ModelSerializer):
    profile_data = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Customer
        fields = '__all__'

    @staticmethod
    def get_profile_data(obj):
        return UserSerializer(obj.profile_number).data if obj.profile_number else None