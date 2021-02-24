from rest_framework import serializers


class NewUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
