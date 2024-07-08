from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from  .serializers import *
from .models import *
@api_view()
def hello_world(request):
    user_obj = user.objects.all()
    serializers = UserSerializer(user_obj, many=True)

    return Response({"status": "200", 'payload':serializers.data})


@api_view(['POST'])
def get_user(request):
   data = request.data
   serializers = UserSerializer(data=request.data)
   if not serializers.is_valid():
       print(serializers.errors)
       return Response({'status':403, 'errors':serializers.errors,'message': 'Something went wrong'})
   serializers.save()
   
   
   return Response({"status": "200", 'payload':serializers.data , 'message': 'data is saved'})

@api_view(['PATCH'])
def update_user(request, id):
    try:
        user_obj = user.objects.get(id=id)
        serializers = UserSerializer(user_obj,data=request.data, partial = True)
        if not serializers.is_valid():
            print(serializers.errors)
            return Response({'status':403, 'errors':serializers.errors,'message': 'Something went wrong'})
        serializers.save()      
   
   
        return Response({"status": "200", 'payload':serializers.data , 'message': 'data is saved'})
    except Exception as e:
        print(e)
        return Response({"status": 403, 'message': 'invalid id'})
    
@api_view(['DELETE'])
def delete_user(request, id):
    try:
        user_obj = user.objects.get(id=id)
        user_obj.delete()
        return Response({"status": "200", 'message': 'data is deleted'})
    except Exception as e:
        print(e)
        return Response({"status": 403, 'message': 'invalid id'})



