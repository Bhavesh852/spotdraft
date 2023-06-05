import json
from rest_framework.views import APIView
from django.contrib import messages
from .serializers import *
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth.models import User
from .models import PDF_Detail, Comment
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'user_auth/index.html')


@login_required(login_url='/')
def home(request):
    return render(request, 'user_auth/home.html')


class RegisterAPI(APIView):

    def post(self, request):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checks for errror input
        if len(username) > 12:
            messages.error(request,"Username must be under 10 charactor.")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request,"password not same.")
            return redirect('/')

        # creating User
        owner = User.objects.create_user(username, email, pass1)
        owner.first_name = fname
        owner.last_name = lname
        owner.save()
        messages.success(request,"Register successfully.")
        return redirect('/')


class LoginAPI(APIView):

    def post(self, request):
        login_name = request.POST['username']
        login_pwd = request.POST['pwd']
        user = authenticate(username=login_name, password=login_pwd)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('/home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/')


class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        messages.success(request, "Successfully logged out.")
        return redirect('/')



class UploadComment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        dataToAdd = request.data
        payload = {
            'pdf_for' : pk,
            'by_user' : request.user.id,
            'comment' : dataToAdd['comment']
        }
        serializer = CommentUploadSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
        else:
            messages.error(request, "Internal error...")
        
        return redirect(f'/comments/{pk}')



class UploadPdf(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        dataToAdd = request.data
        payload = {
            "user" : request.user.id,
            "pdf_title" : dataToAdd['pdf_title'],
            "pdf_description" : dataToAdd['pdf_description'],
            "pdf" : dataToAdd['pdf']
        }
        extension = str(dataToAdd['pdf']).split(".")
        if extension[1].lower() != 'pdf':
            messages.error(request,"Please upload .pdf file.")
            return redirect('/home/')
        
        serializer = PDF_DetailSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()

        messages.success(request, "PDF Added successfully.")
        return redirect('/home/')

@login_required(login_url='/')
def dashboard(request):
    obj = PDF_Detail.objects.all()
    serializer = PDF_Detail_User_Serializer(obj, many=True)
    data = json.loads(json.dumps(serializer.data))
    return render(request, 'user_auth/dashboard.html', {'data': data[::-1]})

@login_required(login_url='/')
def comments(request, pk):
    pdf = PDF_Detail.objects.get(id=pk)
    objs = Comment.objects.filter(pdf_for=pdf)
    serializer = CommentSerializer(objs, many=True)
    data = json.loads(json.dumps(serializer.data))
    return render(request, 'user_auth/comments.html', {'comments' : data, 'pdf' : pdf, 'user' : pdf.user.username})