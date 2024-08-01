from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet): #это специальное представление, которое предоставляет Django Rest Framework. Он будет обрабатывать GET и POST для Heroe без дополнительной работы.
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


import json

# Получите данные из базы данных
heroes = Hero.objects.all()

serializer = HeroSerializer(heroes, many=True)
serialized_data = serializer.data

# Преобразование сериализованных данных в формат JSON
json_data = json.dumps(serialized_data, indent=4)

# Запись данных в файл
with open('heroes.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("Данные успешно сохранены в файл heroes.json")
