from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
import json

from .serializers import HeroSerializer
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet): #это специальное представление, которое предоставляет Django Rest Framework. Он будет обрабатывать GET и POST для Heroe без дополнительной работы.
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

    def delete(self, request, *args, **kwargs):
        Hero.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HeroPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    lookup_field = "pk"


# Получите данные из базы данных
heroes = Hero.objects.all()

serializer = HeroSerializer(heroes, many=True)
serialized_data = serializer.data

json_data = json.dumps(serialized_data, indent=4)

with open('heroes.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("Данные успешно сохранены в файл heroes.json")
