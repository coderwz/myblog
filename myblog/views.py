from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm

def home(request):
    return render(request, 'index.html', {'userstate':request.user.is_authenticated()})

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    # print password, username

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

def loggedin(request):
    return render_to_response('loggedin.html', {'full_name':request.user.username})

def signup(request):
    return render_to_response('signup.html', {})

def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})

    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    return render_to_response('login.html', args)




def logout(request):
    auth.logout(request)
    return render(request, 'logout.html', {})

def invalid(request):
    return render_to_response('invalid.html', {})
