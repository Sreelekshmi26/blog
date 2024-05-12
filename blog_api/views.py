from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm, BlogPostForm
from .models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.order_by('-publication_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_obj': page_obj})

# Home page
def index(request):
    return render(request, 'home.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    blog_posts = Post.objects.all().order_by('-publication_date')
    # Paginate the blog posts
    paginator = Paginator(blog_posts, 10)  # Show 10 blog posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'blog_posts': page_obj})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # Create a new blog post object but don't save it yet
            new_post = form.save(commit=False)
            # Set the author of the blog post to the current user
            new_post.author = request.user
            # Now save the blog post to the database
            new_post.save()
            return redirect('home')  # Redirect to home page after successful creation
    else:
        form = BlogPostForm()
    return render(request, 'post.html', {'form': form})

from django.db.models import Q

def search_posts(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        paginator = Paginator(results, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        results = []
    return render(request, 'home.html', {'blog_posts': page_obj, 'query': query})