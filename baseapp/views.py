
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.fields import JSONField
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

import json
import math
import logging
from django.contrib.auth.models import User
# from .members import members

from .models import Member, Organization, OrganizationPosts,DVDBenchTrainingData, DVDBenchTestingData,  NDBenchTrainingData, NDBenchTestingData
from .serializers import MemberSerializer, MemberSerializerForLogin, UserSerializer, UserSerializerWithToken, OrganizationPostsSerializer, OrganizationSerializer, DVDBenchTrainingDataSerializer, DVDBenchTestingDataSerializer, NDBenchTrainingDataSerializer, NDBenchTestingDataSerializer 
# Create your views here.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.views.generic import ListView, DetailView

from .filters import MemberFilter

logger = logging.getLogger(__name__)

def multiple(*a):
    result = 1
    for i in a:
        result = result * i
    return result




@api_view([ 'POST'])
def getWorkload(request):

    data = request.data
    # print('DATA', data)
    try:   
        # return Response(data['dataType'])
        
        workloadMetric=data['workloadMetric']
        thisdict={}
        res=[]
        if([(data['batchUnit']!=0 )and (data['batchId']!=0 ) and (data['batchSize']!=0 )]):
        # if(True):
            batchUnit=int(data['batchUnit'])
            batchId=int(data['batchId'])
            batchSize=int(data['batchSize'])

            # return Response(batchId*batchUnit)
            startRange=(int(batchId-1)*int(batchUnit))
            startRangeAct=int(startRange)+1
            
            endRange=int(startRange)*int(batchSize)

            rfwId=data['rfwId']
            LastBatchId=batchId+batchSize-1

            thisdict["rfwId"]=rfwId
            thisdict["LastBatchId"]=LastBatchId


            i=0
            if(data['benchmarkType']=='DVD'):
                if(data['dataType']=='Training'):
                    while i <= (batchSize-1):
                        a= DVDBenchTrainingData.objects.filter(_id__range=[(startRange+1),(startRange+batchUnit)])
                        startRange = startRange + batchUnit
                        i=i+1
                        serializer = DVDBenchTrainingDataSerializer(a, many=True)
                        res.append(serializer.data)
                     
                    thisdict["RequestedDataSamples"]=[res]
                    return Response(json.dumps(thisdict))

                else:
                    while i <= (batchSize-1):
                        a= DVDBenchTestingData.objects.filter(_id__range=[(startRange+1),(startRange+batchUnit)])
                        startRange = startRange + batchUnit
                        i=i+1
                        serializer = DVDBenchTestingDataSerializer(a, many=True)
                        res.append(serializer.data)
                     
                    thisdict["RequestedDataSamples"]=[res]
                    return Response(json.dumps(thisdict))
                        
        
            else:
                
                if(data['dataType']=='Training'):
                    while i <= (batchSize-1):
                        a= NDBenchTrainingData.objects.filter(_id__range=[(startRange+1),(startRange+batchUnit)])
                        startRange = startRange + batchUnit
                        i=i+1
                        serializer = NDBenchTrainingDataSerializer(a, many=True)
                        res.append(serializer.data)
                     
                    thisdict["RequestedDataSamples"]=[res]
                    return Response(json.dumps(thisdict))

                else:
                    while i <= (batchSize-1):
                        a= NDBenchTestingData.objects.filter(_id__range=[(startRange+1),(startRange+batchUnit)])
                        startRange = startRange + batchUnit
                        i=i+1
                        serializer = NDBenchTestingDataSerializer(a, many=True)
                        res.append(serializer.data)
                  
                    thisdict["RequestedDataSamples"]=[res]
                    return Response(json.dumps(thisdict))

            
    except:
        message = {'message': 'Invalid details or details already exist'}
        return Response(message,
                        status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def getRoutes(request):
    routes = [
        'api/member/register/',
        'api/member/login/',
        'api/member/updateDetails',

        'api/organization/register',
        'api/organization/login',
        'api/organization/updateDetails',

        'api/organization/createPost',
        'api/organization/assignMember',
        'api/organization/viewMembers',
        'api/organization/viewPosts',
    ]

    return Response(routes)


@api_view(['GET', 'POST'])
def getmembers(request):


    
    return Response('NULL')


class getmemberlist(DetailView):
    Model: Member


# class SpecialDetailView(DetailView):
#     model = Author

    # def get_context_data(self, *args, **kwargs):
    #     context = super(SpecialDetailView, self).get_context_data(
    #         *args, **kwargs)
    #     context['books'] = Book.objects.filter(popular=True)
    # return context
    # def getmemberlist(request):
    #     members = Member.objects.all
    #     serializer = MemberSerializer(members, many=True)
    #     return Response(serializer.data)


@api_view(['GET'])
def getmember(request, pk):
    member = Member.objects.get(_id=pk)
    serializer = MemberSerializer(member, many=False)
    # for i in members:
    #     if i['_id'] == pk:
    #         member = i

    return Response(serializer.data)


# Customization here

    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
    #     # Add custom claims
    #     token['username'] = user.username
    #     token['message'] = 'Hello world'
    #     return token

    # Updating this class
    # def validate(self, attrs):
    #         data = super().validate(attrs)

    #         refresh = self.get_token(self.user)

    #         data['refresh'] = str(refresh)
    #         data['access'] = str(refresh.access_token)

    #         if api_settings.UPDATE_LAST_LOGIN:
    #             update_last_login(None, self.user)

    #         return data
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        # data['username'] = self.user.username
        # data['email'] = self.user.email
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def userRegister(request):
    data = request.data
    # print('DATA', data)
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)    


#
#
##
# New changes


@api_view(['GET', 'POST'])
def memberRegister(request):
    if request.method == 'GET':
        member = Member.objects.all()
        serializer = MemberSerializer(member, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            serializer = MemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            message = {'message': 'Invalid details or details already exist'}
            return Response(message,
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            message = {'message': 'Invalid details or details already exist'}
            return Response(message,
                            status=status.HTTP_400_BAD_REQUEST)

            # serializer.errors


@api_view(['GET', 'POST'])
def memberLogin(request):
    if request.method == 'POST':
        try:
            member = Member.objects.get(email=request.data['email'])
            if(member.password == request.data['password']):
                serializer = MemberSerializer(member, many=False)
                return Response(serializer.data)
            else:
                message = {'message': 'Invalid email id/ password'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        except:
            message = {'message': 'Invalid email id/ password'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
            # return Response(serializer.errors,
            #                 status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def memberHomepage(request):
    return Response()


@api_view(['GET', 'POST'])
def getMemberProfile(request):

    member = Member.objects.get(_id=request.data["_id"])
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def memberUpdateDetails(request):
    data = request.data
    try:
        member = Member.objects.get(_id=data['_id'])

        member.username = data['username']
        member.email = data['email']

        if data['password'] != '':
            member.password = data['password']
        # member.addressStreet = data['addressStreet']
        member.addressLocation = data['addressLocation']
        member.bloodGroup = data['bloodGroup']
        # member.dateOfBirth = data['dateOfBirth']
        # member.paidAt = datetime.now()
        member.save()
        serializer = MemberSerializer(member, many=False)
        return Response(serializer.data)

        # else:
        #     message = {'message': 'Invalid email id/ password'}
        #     return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except:
        message = {'message': 'Invalid details or email already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET', 'POST'])
def memberViewTasks(request):
    data = request.data
    organizationPosts = OrganizationPosts.objects.filter(
        MemberSelected=data['MemberSelected'])
    serializer = OrganizationPostsSerializer(organizationPosts, many=True)
    return Response(serializer.data)


@ api_view(['GET', 'POST'])
def organizationRegister(request):
    if request.method == 'GET':
        organization = Organization.objects.all()
        serializer = OrganizationSerializer(organization, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            serializer = OrganizationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            message = {'message': 'Invalid details or details already exist'}
            return Response(message,
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            message = {'message': 'Invalid details or details already exist'}
            return Response(message,
                            status=status.HTTP_400_BAD_REQUEST)

            # serializer.errors


@api_view(['GET', 'POST'])
def organizationLogin(request):
    if request.method == 'POST':
        try:
            organization = Organization.objects.get(
                email=request.data['email'])
            if(organization.password == request.data['password']):
                serializer = OrganizationSerializer(organization, many=False)
                return Response(serializer.data)
            else:
                message = {'message': 'Invalid email id/ password'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        except:
            message = {'message': 'Invalid email id/ password'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
            # return Response(serializer.errors,
            #                 status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def organizationHomepage(request):
    return Response()


@api_view(['GET', 'POST'])
def getOrganizationProfile(request):
    organization = Organization.objects.get(_id=request.data["_id"])
    serializer = OrganizationSerializer(organization, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def organizationUpdateDetails(request):
    data = request.data
    try:
        organization = Organization.objects.get(_id=data['_id'])

        organization.username = data['username']
        organization.email = data['email']

        if data['password'] != '':
            organization.password = data['password']
        # organization.addressStreet = data['addressStreet']
        organization.addressLocation = data['addressLocation']
        organization.chairman = data['chairman']
        organization.save()
        serializer = OrganizationSerializer(organization, many=False)
        return Response(serializer.data)

    # else:
    #     message = {'message': 'Invalid email id/ password'}
    #     return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except:
        message = {'message': 'Invalid details or email already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def organizationCreatePost(request):
    if request.method == 'POST':
        try:
            data = request.data
            # serializer = OrganizationSerializer(data=data)
            # # if serializer.is_valid():
            # #     serializer.save()
            organization = Organization.objects.get(
                _id=request.data["postedByOrganization"])
            if (data['requirementInformation'] and data['addressLocation']) != '':
                organizationPosts = OrganizationPosts.objects.create(
                    postedByOrganization=organization,
                    postedByOrganizationEmail=data['postedByOrganizationEmail'],
                    requirementInformation=data['requirementInformation'],
                    addressLocation=data['addressLocation']
                )
            serializer = OrganizationPostsSerializer(
                organizationPosts, many=False)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

        except:
            message = {'message': 'Invalid details or enter all details'}
            return Response(message,
                            status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET', 'POST', 'PUT'])
def organizationUpdatePost(request):
    data = request.data
    try:
        organizationPost = OrganizationPosts.objects.get(_id=data['_id'])
        if(data['MemberSelected'] != ''):
            member = Member.objects.get(_id=data['MemberSelected'])
            organizationPost.MemberSelected = member

        if (data['requirementInformation'] and data['addressLocation']) != '':
            organizationPost.requirementInformation = data['requirementInformation']
            organizationPost.addressLocation = data['addressLocation']

        # organization.addressStreet = data['addressStreet']
        organizationPost.save()
        serializer = OrganizationPostsSerializer(organizationPost, many=False)
        return Response(serializer.data)

    # else:
    #     message = {'message': 'Invalid email id/ password'}
    #     return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except:
        message = {'message': 'Invalid details '}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    return Response()


@ api_view(['GET', 'POST'])
def organizationViewMembers(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)


@ api_view(['GET', 'POST'])
def organizationViewPosts(request):
    data = request.data
    organizationPosts = OrganizationPosts.objects.filter(
        postedByOrganization=data['postedByOrganization'])
    serializer = OrganizationPostsSerializer(organizationPosts, many=True)
    return Response(serializer.data)
