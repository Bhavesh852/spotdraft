from rest_framework import serializers
from .models import PDF_Detail, Comment

class PDF_DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PDF_Detail
        fields = '__all__'

class PDF_Detail_User_Serializer(serializers.ModelSerializer):

    class Meta:
        model = PDF_Detail
        fields = '__all__'
        depth = 1

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1


class CommentUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'