from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User


def index(request):
    # User.objects.all() SELECT * from User

    # context = {
    #     'users':  User.objects.all(),
    #
    # }
    return render(request , 'restfulapp/index.html')

#valide
def process(request):
    users = User.objects.all()
    if len(request.POST['first_name']) < 3 and len(request.POST['last_name']) < 3 and len(request.POST['email']) < 3:
        print "no"
    else:
        newuser = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email']
        )
        print newuser.first_name
        print newuser

    return redirect('/')


def checkusers(request):
    context = {
        'users':  User.objects.all()
        # 'showuser_id' : User.objects.get(id=user_id)

    }

    return render( request, 'restfulapp/users.html', context)

def create_user(request):
    User.objects.checkfirst(request, request.POST)
    return redirect('/')

def showuser(request,id):
    user = User.objects.get(id=id)
    return render(request, 'restfulapp/userid.html', {'user':user})
