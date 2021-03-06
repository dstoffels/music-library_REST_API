from django.http import Http404
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SongList(APIView):
  def get(self, request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetail(APIView):
  def get_song(self, id):
    try:
      return Song.objects.get(pk=id)
    except Song.DoesNotExist:
      raise Http404

  def get(self, request, id):
    song = self.get_song(id)
    serializer = SongSerializer(song)
    return Response(serializer.data)

  def put(self, request, id):
    song = self.get_song(id)
    serializer = SongSerializer(song, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    song = self.get_song(id)
    song.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class SongLike(APIView):
  def get_song(self,id):
    try:
      return Song.objects.get(pk=id)
    except Song.DoesNotExist:
      raise Http404

  def put(self, request, id):
    song = self.get_song(id)
    song.like()
    serializer = SongSerializer(song)
    return Response(serializer.data)