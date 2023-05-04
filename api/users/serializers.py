from .models import MyUser
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    #name = serializers.CharField()
    #city = serializers.CharField()
    email = serializers.CharField()
    age = serializers.IntegerField()
    password = serializers.CharField()

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('email', instance.name)
        instance.city = validated_data.get('age', instance.city)
        instance.password = validated_data.get('password', instance.city)

        instance.save()
        return instance
