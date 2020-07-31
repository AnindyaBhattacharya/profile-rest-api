from rest_framework import serializers
from . import models


class NameField(serializers.Serializer):
    """ This a rest_frameword serializer, this is similar to Django Forms"""
    name = serializers.CharField(max_length=10)


class MyUserSerializers(serializers.ModelSerializer):
    ''' Similar to models.Forms, creates a form out of the model defined'''
    class Meta:
        model = models.MyUser
        fields = ('id', 'email', 'username', 'DOB', 'password')
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        user_obj = models.MyUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            DOB=validated_data['DOB'],
            password=validated_data['password'],
        )
        return user_obj


class UserStatusFeedSerializer(serializers.ModelSerializer):
    ''' Creating froms out of UserStatusSerializers '''
    class Meta:
        model = models.UserStatusFeed
        fields = ('id', 'user_profile_id', 'status_feed', 'created_date')
        extra_kwargs = {'user_profile_id': {'read_only': True}}
