from rest_framework import serializers
# model
from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields = '__all__'


class AuthorRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'full_name': str(instance)
        }
    