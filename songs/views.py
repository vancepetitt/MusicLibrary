from logging import raiseExceptions
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer
from rest_framework import status
from .models import Song
from songs import serializers

@api_view(['GET', 'POST'])
def songs_list(request):

    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
