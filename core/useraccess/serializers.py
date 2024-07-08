from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        exclude = ['confirm_password']

    def validate(self, data):
        if 'name' in data and data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error": "Name should not contain numbers"})
        return data