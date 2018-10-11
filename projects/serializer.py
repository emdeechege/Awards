from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profile_photo','bio','phone')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields =('title','posted_by', 'description')
