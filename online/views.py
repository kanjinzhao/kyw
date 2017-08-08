#coding=utf-8

from django import forms
from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from models import User

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def regist(req):
    if req.method == "POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            passwd = uf.cleaned_data['password']
            #print username,passwd
            #将username,passwd写入数据库语
            User.objects.create(username=username,password=passwd)
            #设置跳转页面，并传递cookies
            response = HttpResponseRedirect('/index')
            response.set_cookie('username', username, 3600)
            return response
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf})


def login(req):
    if req.method == "POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            passwd = uf.cleaned_data['password']
            users = User.objects.filter(username__exact=username,password__exact=passwd)
            if users:
                response = HttpResponseRedirect('/index')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})

def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html',{'username':username})


def logout(req):
    response = HttpResponseRedirect('/login')
    response.delete_cookie('username')
    return response
