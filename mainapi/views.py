from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Product,Sales
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer,ProductSerializer
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.backends import smtp 
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def product_list(request):
  
    if request.method == 'GET':
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
            
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

@csrf_exempt
def buydish(request , pk):
    if request.method == 'PUT':
        snippet = Product.objects.get(id=pk) 
        
        snippet.product_stock = int(snippet.product_stock) - 1
        snippet.save()
        send_mail("hello ","Total Availabel Stock Of "+ snippet.product_name +" is "+ str(snippet.product_stock) , "mohamedarshadcholasseri5050@gmail.com", ["vyshnuakku@gmail.com"])
        sales = Sales.objects.create(product=snippet)
        return JsonResponse({"Available Stock":snippet.product_stock,"sales No":sales.id}, status=201)
    return JsonResponse(serializer.errors, status=400)