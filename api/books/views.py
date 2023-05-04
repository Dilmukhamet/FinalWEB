from django.shortcuts import render
from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_genre(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))    
def genre_by_id(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        genre.delete()
        return HttpResponse(status=204)
    
#-----------------------------BOOK_API----------------------------

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def book_list(request):
    data = JSONParser().parse(request)
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes((AllowAny,))
def genre_list_view(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return JsonResponse(serializer.data, safe=False)


class book_list_view(APIView):
    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)      
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return JsonResponse(serializer.data, safe=False)
    '''def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''



class bookById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"
    permission_classes = (IsAuthenticated,)

    

    

class book_by_id(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    
    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET']) 
@permission_classes((AllowAny,))
def books_by_genre(request, id):
    books = Genre.objects.get(id=id).books.all()
    serializer = GenreSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)