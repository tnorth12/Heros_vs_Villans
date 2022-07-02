# from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from .models import SuperType



# Views

@api_view(['GET', 'POST'])
def supertypes_list(request):

    if request.method == 'GET':
        supertypes = SuperType.objects.all()
        serializer = SuperTypeSerializer(supertypes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])
# def supertypes_detail(request, pk):
#     supertypes = get_object_or_404(supertypes, pk=pk)
#     if request.method == 'GET':
#         serializer = SuperTypeSerializer(supertypes)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = SuperTypeSerializer(supertypes, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         supertypes.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)