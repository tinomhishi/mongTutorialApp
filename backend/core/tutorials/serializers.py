from rest_framework import serializers
from tutorials.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'is_published',
                  'created_by',)

        extra_kwargs = {
            'created_by': {'required': False},}
