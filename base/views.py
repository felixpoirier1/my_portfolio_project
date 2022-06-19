from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Project, FilePath
import os
#import seaborn as sns
#import matplotlib.pyplot as plt
#from .portfolio import Portfolio

# Create your views here.
def home(request):
    projects = Project.objects.all()
    name = request.POST.get('name')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    from_email = request.POST.get('from_email')

    content = '''
    {}
    \t
    \t
    From {}
    \t
    Email {}
    '''.format(message, name, from_email)

    if subject and message and from_email:
        try:
            send_mail(subject, content, from_email, ['felixpoirier2001@gmail.com'], fail_silently = False)
            del name
            del subject
            del message
            del from_email

        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    context = {'projects': projects}
    return render(request, 'home.html', context)

def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    files = project.filepath_set.all()
    context = {'project': project, 'files': files}
    return render(request, 'project-details.html', context)
'''
def portfolioOpt(request):

    def displayWeights(df):
        return sns.catplot(kind = 'bar', x='pct', y = 'index', data=df.transpose().reset_index()).set(ylabel="ticker")

    
    real_path = os.path.realpath(__file__)
    dir_path = os.path.dirname(real_path)
    os.chdir(dir_path)
    print(os.getcwd())
    print(os.listdir('STOCKS'))
    ####
    sec = input("Pick a sector : ")
                        
    cont = True
    stock_list = [] 
    path = f'STOCKS/{sec.upper()}/'

    ####
    while cont:
        choice = input("Pick a stock or stop [0]: ")
        
        if choice == '0':
            cont = False
        else:
            stock_list.append(choice)    
    ####    
        
    lol=Portfolio(stocks=stock_list, directory = path, local = True).optimize()
    return render(request, 'portfolio-opt.html')'''
