from django.shortcuts import render
from functools import lru_cache
from . import prices
from django import forms
from django.utils.translation import ugettext as _
from django.contrib import auth
from django.shortcuts import redirect
import requests
import mysql.connector

class UserLoginForm(forms.Form):
    username = forms.CharField(label=_(u'Username'), max_length=30)
class RegForm(forms.Form):
    name = forms.CharField(label=_(u'name'), max_length=30)
    password = forms.CharField(label=_(u'password'), max_length=30)
class LoginForm(forms.Form):
	login = forms.CharField(label=_(u'login'), max_length=30)
	password = forms.CharField(label=_(u'password'), max_length=30)

def start(request):
	a = request.environ['REMOTE_ADDR']
	print(a)
	return render(request, 'start_page.html')


def user_login_view(request,):
	form = UserLoginForm(request.POST or None)
	print(form)
	context = { 'form': form}
	if request.method == 'POST' and form.is_valid():
		username = form.cleaned_data.get('username', None)
		'''result_ch = prices.take_prices_for_chitay_gorod(username)
		result_lab = prices.take_prices_for_labirint(username)
		'''
		result = prices.take_prices_for_labirint(username)
		return render(request, 'steve_jobs.html', {'res':result, 'username': username})
	else:
		return render(request, 'test.html', context)


def registration(request):
	form = RegForm(request.POST or None)
	print(form)
	if request.method == 'POST':
		name = form.cleaned_data.get('name', None)
		password = form.cleaned_data.get('password', None)
		print(name, password)
		name_true = "'" + name + "'"
		password_true = "'" + password + "'"
		cnx = mysql.connector.connect(user='root', password='root',
	                              host='127.0.0.1',
	                              database='testik')
		cursor = cnx.cursor()

		reg = ("""
			INSERT INTO 
				users (name, password) 
			VALUES ({}, {});
			""".format(name_true,password_true))
		cursor.execute(reg)
		cnx.commit()
		cnx.close()
		return render (request, 'result.html')
	else:	
		return render(request, 'registr.html')

def login_up(request):
	form = LoginForm(request.POST or None)
	log_true = ''
	print(form, request.method)
	if request.method == 'POST':
		login = form.cleaned_data.get('login', None)
		password = form.cleaned_data.get('password', None)
		login = "'" + login + "'"
		password = "'" + password + "'"
		print(login, password)
		cnx = mysql.connector.connect(user='root', password='root',
	                              host='127.0.0.1',
	                              database='testik')
		cursor = cnx.cursor()

		reg = ("""
				SELECT password FROM 
					testik.users
				WHERE
					name = {}
				""").format(login)
		cursor.execute(reg)
		res = cursor.fetchall()
		for i in login:
			if i == "'":
				pass
			else:
				log_true += i
		if res:
			res = "'" + res[0][0] + "'"
			print(res)
			if res == password:
				cnx.commit()
				cnx.close()
				return render(request, 'result2.html', {'log': log_true})
			else:
				return render (request, 'login.html')
		elif request.method == 'GET':
			return render (request, 'login.html')
	else:
		return render(request, 'login.html')

