from rest_framework import serializers, status

from django.contrib.auth import get_user_model

from .utility import get_city_and_country_from_pincode
# User Registration Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'phone_number', 'address', 'pin_code', 'city', 'country']
        extra_kwargs = {'password': {'write_only': True}}
        ref_name = 'CustomUserSerializer'

    def validate(self, attrs):
        pin_code = attrs.get('pin_code', None)
        if pin_code:
            city, country = get_city_and_country_from_pincode(pin_code)
            if city and country:
                attrs['city'] = city
                attrs['country'] = country
        return attrs

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        user.phone_number = validated_data['phone_number']
        user.address = validated_data['address']
        user.pin_code = validated_data['pin_code']
        user.city = validated_data['city']
        user.country = validated_data['country']
        user.save()
        return user