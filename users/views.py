from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth.hashers import make_password

class Signup(APIView):

    serializer_class = LoginSerializer

    def post(self, request, fomrat=None):
        """"
        login logic
        """

        # serializeing and validating data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # make password to save user
        hashed_password = make_password(serializer.validated_data.get("password"))
        serializer.save(password=hashed_password)
    

class OauthCallback(APIView):

    def get(self, request, format=None):
        """
        after user login to the account using oauth the uri redirected to this page.
        it contains refresh tocken and this function is generate a accesstocken using refresh tocken
        to create tocken send the refresh ocken to the auth server
        """
        pass



        
