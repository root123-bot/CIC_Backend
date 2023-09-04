from .models import *
from rest_framework.serializers import ModelSerializer

class RawPostSerializer(ModelSerializer):
    class Meta:
        model = RawPost
        fields = [
            'id',
            'title',
            'content',
            'date_posted'
        ]