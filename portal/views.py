from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import ProductSerializer, UserSerializer, RegisterSerializer, LoginSerializer, ProductSerializer
from django.contrib.auth.models import User
from knox.models import AuthToken
from django.core.mail import send_mail



class RegisterView(generics.GenericAPIView):
       
       serializer_class = RegisterSerializer

       def post(self, request, *args, **kwargs):
              serializer = self.get_serializer(data=request.data)
              serializer.is_valid(raise_exception=True)
              user = serializer.save()
              return Response({
                     "user": UserSerializer(user, context=self.get_serializer_context()).data,
                     "token":AuthToken.objects.create(user)[1]
              })


class LoginView(generics.GenericAPIView):
       
       serializer_class = LoginSerializer

       def post(self, request, *args, **kwargs):
              serializer = self.get_serializer(data=request.data)
              serializer.is_valid(raise_exception=True)
              user = serializer.validated_data
              return Response({
                     "user": UserSerializer(user, context=self.get_serializer_context()).data,
                     "token":AuthToken.objects.create(user)[1]
              })


class Portal(APIView):

       permission_classes = [permissions.IsAuthenticated]

       def get(self, request):
              return Response({"Get Works":"Yes 200"})


       def post(self, request):

              sender_email = request.user.email

              serializer = ProductSerializer(data=request.data)

              if serializer.is_valid():
                     serializer.save()
                     
              
                     product_name = request.data['product_name']
                     product_detail = request.data['product_detail']
                     product_price = request.data['product_price']

                     send_mail(
                            f"From {request.user} Email {sender_email}",
                            f""" 
                                   Product Title : {product_name} \n
                                   Product Description : {product_detail} \n 
                                   Producy Prize : {product_price}
                            """,
                            'Put Your email adress here',
                            ['Put Your email adress here'],
                            fail_silently=False,
                     )

                     return Response(serializer.data)

              return Response(serializer.error_messages)
              