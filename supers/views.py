from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import super_types
from super_types.models import SuperType
from .serializers import SuperSerializer
from .models import Super



# Views

@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == 'GET':
        supers_type = request.query_params.get('super_type')                  #query_parma ? to return super_type 
        # print(supers_type)

        supers = Super.objects.all()
        

        if supers_type:
            supers = supers.filter(super_type__super_type=supers_type)         #class desingation in each apps model was confusing
        
                
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # custom_response_dictionary = {}                                                            # Trying this out, but had some difficulty 

    # for super_type in super_types:
    #     supers = supers.filter(super_type__super_type=super_type)
    #     serializer = SuperSerializer(supers, many=True)

    #     custom_response_dictionary[super_types.super_type] = {
    #         "Heros": [],
    #         "Villians": []


    #     }
       
   

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        
        serializer = SuperSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

