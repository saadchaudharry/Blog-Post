from django.shortcuts import render, HttpResponseRedirect
from .forms import signupForm, loginForm, PostForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import blogPost
from django.contrib.auth.models import Group

# Create your views here.

# -----------------------home---------------------
def home(request):
    posts = blogPost.objects.all()
    context = {'posts':posts, 'home':'active'}
    return render(request, 'mblog/home.html', context)

# -------------------About------------------
def about(request):
    return render(request, 'mblog/about.html', {'about':'active'})

# ----------------------Contact----------------------
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Send Successfully !!')
    else:
        form = ContactForm()        
    return render(request, 'mblog/contact.html', {'form':form, 'contact':'active'})

# ---------------------Dashboard-------------------
def dashboard(request):
    if request.user.is_authenticated:
        posts = blogPost.objects.all()
        full_name = request.user.get_full_name()
        gps = request.user.groups.all()
        context = {'posts':posts, 'name':request.user.username, 'full_name':full_name, 'groups':gps, 'dashboard':'active'}
        return render(request, 'mblog/dashboard.html', context)
    else:
        return HttpResponseRedirect('/login/')

# ------------------------SignUp--------------------------
def user_signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have become an author.')
            user = form.save()
            group = Group.objects.get(name='Author') # isse group ko get krlege
            user.groups.add(group) # user ko group me daal dege
    else:
        form = signupForm()

    context = {'form':form, 'signup':'active'}            
    return render(request, 'mblog/signup.html', context)

# ------------------------Login---------------------
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = loginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username'] 
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !! ')
                    return HttpResponseRedirect('/dashboard/') 
        else:
            form = loginForm()
        context = {'form':form, 'login':'active'}        
        return render(request, 'mblog/login.html', context)
    else:
        return HttpResponseRedirect('/dashboard/')
# ------------------------------Logout-----------------------
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# ------------------------------Add New Post-----------------------

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Added Successfully !!')
        else:
            form = PostForm()           
        return render(request, 'mblog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

# ------------------------------Update/Edit Post-----------------------

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = blogPost.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, 'Updated Successfully !!')
        else:
            pi = blogPost.objects.get(pk=id)
            form = PostForm(instance=pi)        
        return render(request, 'mblog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

# ------------------------------Delete  Post-----------------------

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = blogPost.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
