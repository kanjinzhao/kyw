#coding=utf-8

from django import forms
from django.http import  HttpResponse
from django.shortcuts import render_to_response
from models import User

class UserForm(forms.Form):
    username = forms.CharField()
    passwd = forms.CharField(widget=forms.PasswordInput)

def regist(req):
    if req.method == "POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            passwd = uf.cleaned_data['passwd']
            #print username,passwd
            #将username,passwd写入数据库语
            User.objects.create(username=username,password=passwd)
            return HttpResponse('ok')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf})