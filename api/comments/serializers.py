from .models import Comment
from rest_framework import serializers
from books.serializers import BookSerializer
from books.models import Book
from users.models import MyUser
from users.serializers import UserSerializer

    
class CommentSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    book = BookSerializer(read_only=True)
    #user = UserSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True)
    #user_id = serializers.IntegerField(write_only=True)
    #serialuzer = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Comment
        #fields = ['text', 'rating', 'user', 'user_id', 'book', 'book_id']
        fields = ['text', 'rating', 'book', 'book_id']
    
    def validate(self, attrs):
        if 'book' in attrs:
            book = Book.objects.filter(id=attrs['book_id']).first()
            if not book:
                raise serializers.ValidationError("Book does not exist")
        '''if 'user' in attrs:
            user = MyUser.objects.filter(id=attrs['user_id']).first()
            if not user:
                raise serializers.ValidationError("User does not exist")'''
        return attrs