from rest_framework import serializers
from .models import WatchList, StreamPlatform

class WatchListSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    storyline = serializers.CharField(max_length=100)
    # platform = serializers.ForeignKey(StreamPlatform, on_delete=models.CASCADE)
    active = serializers.BooleanField(default = True)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.storyline = validated_data.get('storyline', instance.storyline)
        instance.active = validated_data.get('active', instance.active)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

class StreamPlatformSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    about = serializers.CharField(max_length=100)
    website = serializers.URLField(max_length=100)

    def create(self, validated_data):
        return StreamPlatformSerializer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.website = validated_data.get('website', instance.website)
        instance.save()
        return instance
