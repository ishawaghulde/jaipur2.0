from rest_framework import serializers
from polls.models import login_user, feedback1_routes, feedback1_text

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= login_user
        fields="__all__"


class feedbackRoutesSerializer(serializers.ModelSerializer):
    class Meta:
         model= feedback1_routes
         fields="__all__"


class feedbackTextSerializer(serializers.ModelSerializer):
    class Meta:
         model= feedback1_text
         fields="__all__"

