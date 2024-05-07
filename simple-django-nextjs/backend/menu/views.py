from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .serializers import MenuSerializer
from django.shortcuts import get_object_or_404
from .models import Menu
from .filters import MenuFilter

# Create your views here.
@api_view(['GET'])
def getAllMenu(request):

    filterset = MenuFilter(request.GET, queryset=Menu.objects.all().order_by('id'))

    count = filterset.qs.count()
    resPerPage = 3
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset.qs, request)


    serializer = MenuSerializer(queryset, many=True)
    return Response({
        "count": count,
        "resPerPage": resPerPage,
        'item': serializer.data
        })

@api_view(['POST'])
def addMenu(request):
    data = request.data

    menu = Menu.objects.create(**data)

    serializer = MenuSerializer(menu,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getMenu(request, pk):
    menu = get_object_or_404(Menu, id=pk)

    serializer = MenuSerializer(menu, many=False)

    return Response(serializer.data)

@api_view(['PUT'])
def updateMenu(request, pk):
    menu = get_object_or_404(Menu, id=pk)

    # Check if the request contains 'name' and 'price' keys
    if 'name' in request.data and 'price' in request.data:
        name = request.data['name']
        price = request.data['price']

        # If the name is "kontol", set the price to 170000
        if name == "kontol":
            price = 170000

        # Pass the data when creating the serializer instance
        serializer = MenuSerializer(menu, data={'name': name, 'price': price})

        # Check if the serializer is valid after passing the data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    # Return a bad request response if the data is invalid or incomplete
    return Response({'error': 'Invalid data or missing fields'}, status=status.HTTP_400_BAD_REQUEST)
