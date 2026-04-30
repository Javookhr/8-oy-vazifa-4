from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import StringRelatedField, PrimaryKeyRelatedField, HyperlinkedRelatedField, SlugRelatedField, HyperlinkedIdentityField

from .models import Car,Drive

USer = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8,max_length=126)

    class Meta:
        model = USer
        fields = ('username','email','password')

    def validate_username(self,value):
        if USer.objects.filter(username=value).exists():
            raise serializers.ValidationError('Bu usernamedagi foydalanuvchi allaqachon mavjud')
        return value

    def validate_email(self,value):
        if "@" not in value and "." not in value:
            raise serializers.ValidationError("email noto'g'ri")
        return value
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password !=password2:
            raise serializers.ValidationError({
                "password":"Parollar bir biriga mos emas !"
            })

        return attrs
    def create(self,validate_data):
        password2 = validate_data.app('password2')

        return  USer.objects.create_user(**validate_data)


class CarSerializer(serializers.ModelSerializer):
    owner_string = StringRelatedField(source='owner', read_only=True)
    owner_id = PrimaryKeyRelatedField(source='owner', queryset=USer.objects.all())
    owner_url = HyperlinkedRelatedField(source='owner', view_name='user-detail', queryset=USer.objects.all())
    slug_field = SlugRelatedField(source='owner', slug_field='username', queryset=USer.objects.all())

    class Meta:
        model = Car
        fields = ('id', 'name', 'color', 'year', 'owner_string', 'owner_id', 'owner_url', 'slug_field')
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


class DriveSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)
    car_name = serializers.CharField(source='car.name', read_only=True)

    class Meta:
        model = Drive
        fields = ('id', 'name', 'phone', 'price', 'age', 'car', 'car_name')

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

class DriveHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='drive-detail')

    class Meta:
        model = Drive
        fields = ('url', 'id', 'name', 'phone', 'price', 'age')

