from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializers a name filed for testing our APIview."""

    name = serializers.CharField(max_length=10)