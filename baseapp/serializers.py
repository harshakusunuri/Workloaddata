from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Member
from .models import Organization
from .models import OrganizationPosts
from .models import DVDBenchTrainingData
from .models import DVDBenchTestingData
from .models import NDBenchTrainingData
from .models import NDBenchTestingData

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class MemberSerializerForLogin(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    # isOrganizationMember = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Member
        fields = ['_id', 'email', 'password', 'isOrganizationMember']

    def get__id(self, obj):
        return obj._id

    def get_isOrganizationMember(self, obj):
        return obj.isOrganizationMember

    # def get_name(self, obj):
    #     name = obj.username
    #     if name == '':
    #         name = obj.email
    #     return name


# class MemberSerializerWithToken(MemberSerializer):
#     token = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Member
#         fields = ['_id', 'username', 'email', 'isOrganizationMember', 'token']

#     def get_token(self, obj):
#         token = RefreshToken.for_user(obj)
#         return str(token)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPosts
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.username
        if name == '':
            name = obj.email
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)






class DVDBenchTrainingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DVDBenchTrainingData
        fields = '__all__'


class DVDBenchTestingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DVDBenchTestingData
        fields = '__all__'


class NDBenchTrainingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NDBenchTrainingData
        fields = '__all__'


class NDBenchTestingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NDBenchTestingData
        fields = '__all__'

        

