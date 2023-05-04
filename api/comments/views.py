from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Comment
from books.models import Book
from django.http import Http404
from rest_framework.views import APIView
from books.serializers import BookSerializer
from rest_framework import status
from rest_framework import generics
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny 

# Create your views here.

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def comment_list(request):
    data = JSONParser().parse(request)
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)



class CommentList(generics.ListCreateAPIView):
   # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        #return super().perform_create(serializer)
        serializer.save(user=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

@api_view(['GET'])
@permission_classes((AllowAny,))
def comment_for_book(request, id):
    comments = Book.objects.get(id=id).comments.all()
    serializer = CommentSerializer(comments, many=True)
    return JsonResponse(serializer.data, safe=False)



'''
class comment_list(APIView):
    def get(self, request, format=None):
        comment =  Comment.objects.all()
        serializer = BookSerializer(comment, many = True)
        return JsonResponse(serializer.data)
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class comments_by_id(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = BookSerializer(comment)
        return JsonResponse(serializer.data)
    
    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)