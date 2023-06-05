from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class home(View):

    def get(self, request):
        return render(request,'home/index.html')
    
class about(View):
    def get(self, request):
        return render(request,'home/about.html')

class reservation(View):
    def get(self, request):
        return render(request,'home/reservation.html')


class deals(View):
    def get(self, request):
        return render(request,'home/deals.html')


class login(View):
    def get(self, request):
        return render(request,'home/login.html')