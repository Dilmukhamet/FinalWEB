from .models import Genre, Book
from rest_framework import serializers


#make usual serializer
class GenreSerializer(serializers.ModelSerializer):
    #company = CompanySerializer(read_only=True)
    #company_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Genre
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    genre = GenreSerializer(read_only=True)
    genre_id = serializers.IntegerField(write_only=True)
    #serialuzer = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'price', 'pic', 'genre', 'genre_id']
    
    def validate(self, attrs):
        if 'genre' in attrs:
            genre = Genre.objects.filter(id=attrs['genre_id']).first()
            if not genre:
                raise serializers.ValidationError("Genre does not exist")
        return attrs

