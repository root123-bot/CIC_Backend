from rest_framework.serializers import ModelSerializer
from .models import *


class ResearcherProfileSerializer(ModelSerializer):
    class Meta:
        model = ResearcherProfile
        fields = [
            'id',
            'name',
            'created_at',
            'updated_at',
            'phone_number',
            'get_image',
            'get_user_id',
            'usergroup',
            'is_active',
            'profile_is_completed',
            'physical_address'
        ]