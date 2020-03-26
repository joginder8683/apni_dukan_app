from django.shortcuts import render
from rest_framework.response import Response
from  rest_framework import status
from  rest_framework.decorators import api_view
from .shopImpl import Shopping


@api_view(['POST'])
def add_product(request):
    data=request.data
    obj=Shopping(data)
    result=obj.add_product()
    return Response(result,status=status.HTTP_200_OK)

@api_view(['POST'])
def add_coupon(request):
    data=request.data
    obj=Shopping(data)
    result=obj.add_coupon()
    return Response(result,status=status.HTTP_200_OK)

@api_view(['POST'])
def add_product_in_cart(request):
    data=request.data
    obj=Shopping(data)
    result=obj.add_product_in_cart()
    return Response(result,status=status.HTTP_200_OK)


@api_view(['POST'])
def create_order(request):
    data=request.data
    obj=Shopping(data)
    result=obj.create_order()
    return Response(result,status=status.HTTP_200_OK)



