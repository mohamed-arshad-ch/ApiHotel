from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','first_name','last_name']
        extra_kwargs = {'password':{'write_only':True,'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_name','product_price','product_stock']

    def create(self, valid_data):
        return Product.objects.create(**valid_data)


    def update(self, instance, validated_data):
       
        print(instance)

        
        instance.product_stock = int(instance.product_stock) - 1
        instance.save()
        return instance
