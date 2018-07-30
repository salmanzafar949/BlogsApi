from rest_framework import serializers
from .models import Blog

class BlogSerialize(serializers.ModelSerializer):

    class Meta:
        model = Blog
        # fields = ('title', 'body', 'date')
        fields = '__all__'