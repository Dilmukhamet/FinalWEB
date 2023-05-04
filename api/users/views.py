from django.shortcuts import render
from .serializers import UserSerializer
from .models import MyUser
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.
@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
    

'''
@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        companies = User.objects.all()
        serializer = UserSerializer(companies, many=True)
        return JsonResponse( serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_by_id(request, id):
    try:
        company = User.objects.get(id=id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = UserSerializer(company)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        company.delete()
        return HttpResponse(status=204)
'''
