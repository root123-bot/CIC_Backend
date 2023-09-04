from rest_framework.serializers import ModelSerializer
from .models import *


class MkulimaProfileSerializer(ModelSerializer):
    class Meta:
        model = MkulimaProfile
        fields = [
            'id',
            'name',
            'created_at',
            'updated_at',
            'phone_number',
            'get_image',
            'get_user_id',
            'usergroup',
            'is_active'
        ]