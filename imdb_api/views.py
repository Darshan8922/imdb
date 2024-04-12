
from django.shortcuts import render
from .models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def movie_list(request):
    movie_list = WatchList.objects.all()
    serialized = WatchListSerializer(movie_list, many=True)
    print(movie_list)
    return JsonResponse(serialized.data, safe = False)

def movie_detail(request, pk):
    movie = WatchList.objects.get(pk = pk)
    print(movie)
    serialized = WatchListSerializer(movie)
    return JsonResponse(serialized.data, safe = False)

# @csrf_exempt
# def stream_list(request):
#     if request.method == 'GET':
#         stream_list = StreamPlatform.objects.all()
#         serialized = StreamPlatformSerializer(stream_list, many=True)
#         return JsonResponse(serialized.data, safe = False)
#
#     elif request.method == 'POST':
#         data_get = StreamPlatformSerializer(data=request.data)
#         if data_get.is_valid():
#             data_get.save()
#             return JsonResponse(data_get.data, status=200)
#         return JsonResponse(data_get.errors, status=400)
#
#     elif request.method == 'PUT' or request.method == 'PATCH':
#         try:
#             # Retrieve existing StreamPlatform object based on ID
#             obj = StreamPlatform.objects.get(id=request.data['id'])
#         except StreamPlatform.DoesNotExist:
#             return JsonResponse({'error': 'StreamPlatform does not exist'}, status=404)
#
#         # Create a serializer instance using the retrieved object
#         serializer = StreamPlatformSerializer(obj, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def stream_list(request):
    if request.method == 'GET':
        stream_list = StreamPlatform.objects.all()
        serialized = StreamPlatformSerializer(stream_list, many=True)
        return JsonResponse(serialized.data, safe=False)

    elif request.method == 'POST':
        serializer = StreamPlatformSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT' or request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            obj = StreamPlatform.objects.get(id=data['id'])
        except StreamPlatform.DoesNotExist:
            return JsonResponse({'error': 'StreamPlatform does not exist'}, status=404)
        except KeyError:
            return JsonResponse({'error': 'ID field is required'}, status=400)

        serializer = StreamPlatformSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

def stream_detail(request, pk):
    stream_platform = StreamPlatform.objects.get(pk = pk)
    serialized = StreamPlatformSerializer(stream_platform)
    return JsonResponse(serialized.data, safe = False)














