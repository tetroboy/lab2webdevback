from rest_framework import serializers
from .models import Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'text', 'translation', 'created_at']