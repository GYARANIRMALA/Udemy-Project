from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


# ModelSerializers:
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"
    

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    # len_name = serializers.SerializerMethodField()
    platform = serializers.CharField(source='platform.name')
    
    
    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ["active"]
        
        
class SteamPlatformSerializer(serializers.ModelSerializer):
    WatchList = WatchListSerializer(many=True, read_only=True)
    # WatchList = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='WatchList-detail'
    # )
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"


        

        
    ## VALIDATIONS ##    
    
    # def get_len_name(self, object):
    #     length = len(object.name)
    #     return length
            
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Description should be different!")
    #     else:
    #         return data
         
    # def validate_name(self, value):      
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value
    


# Serializers:

# def name_length(value):
#     if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
                
# class WatchListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return WatchList.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.name = validated_data.get('description', instance.description)
#         instance.name = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should be different!")
#         else:
#             return data
         
    # def validate_name(self, value):
        
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value
        
        