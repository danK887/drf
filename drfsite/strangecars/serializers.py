from rest_framework import serializers
from .models import Cars

class CarsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cars
        fields = "__all__"

# class CarsSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     categor_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Cars.objects.create(**validated_data)