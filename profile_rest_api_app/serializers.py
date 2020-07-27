from rest_framework import serializers

class NameField(serializers.Serializer):
    """ This a rest_frameword serializer, this is similar to Django Forms"""
    name = serializers.CharField(max_length=10)
