from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Car,Drive

USer = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = USer
        fields = ('username','email',pa)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name','color','year')
        read_only_fields = ('id',)


    def validate_name(self,value):
        if not value.istitle():
            raise serializers.ValidationError("ismni bosh harfi kattada bolishi kerak")

        if not value.isalpha():
            raise serializers.ValidationError("Ism faqat harflardan tashkil topgan bolishi kerak")

        return value

    def validate_color(self,value):
        if not value.istitle():
            raise serializers.ValidationError("Color bosh harfi kattada bolishi kerak")

        if not value.isalpha():
            raise serializers.ValidationError("Color faqat harflardan tashkil topgan bolishi kerak")

        return value

    def validate_year(self,value):
        if not value.isdigit():
            raise serializers.ValidationError("Yil faqata sondan iborat bolishi kerak")

        return value

class CarAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name','color','year')
        read_only_fileds = ('id')

#-----------------------Drive----------------------------------------------------------------

class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = ('name','phone','price','age')
        read_only_fields = ('id',)

    def validate_name(self,value):
        if not value.istitle():
            raise serializers.ValidationError("Ismni bosh harfi katta bilan yozilishi kerak")

        if not value.isalpha():
            raise serializers.ValidationError("Ism faqat harflardan tashkil topgan bolishi kerak")

        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Telefon raqam sonlardan ivorat bolishi kerak")

        if not value.startswith('998'):
            raise serializers.ValidationError("Telefon raqam boshi 998 bilan boshlanishi kerak")

        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("summa 0 dan katta bolishi kerak")

        if value >= 100000:
            raise serializers.ValidationError("Summa 100000 kichik bolishi kere")

        return value

    def validate_age(self,value):
        if not value > 15 and value < 100:
            raise serializers.ValidationError("Yosh 15 dan katta bolishi va 100 dan kichik bolishi kerak")

        return value

class DriveAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name','phone','price','age')
        read_only_fileds = ('id')

