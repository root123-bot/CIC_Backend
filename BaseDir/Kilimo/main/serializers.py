from .models import *
from rest_framework.serializers import ModelSerializer

class RawPostSerializer(ModelSerializer):
    class Meta:
        model = RawPost
        fields = [
            'id',
            'title',
            'content',
            'category',
            'date_posted',
            'date_updated',
            'posted_media',
            'get_is_published',
            'is_draft',
            'drafted_by',
            'get_researcher',
        ]