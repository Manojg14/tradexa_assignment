from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Post
from .forms import RegisterForm, LoginForm, PostForm
from products.models import Product


def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper


def register_view(request):
    if request.session.get('user_id'):
        return redirect('dashboard')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = User(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            username=form.cleaned_data['username'],
        )
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(request, "Account created! Please log in.")
        return redirect('login')
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.session.get('user_id'):
        return redirect('dashboard')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                messages.success(request, f"Welcome back, {user.first_name}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid password.")
        except User.DoesNotExist:
            messages.error(request, "User not found.")
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('login')


@login_required_custom
def dashboard_view(request):
    user = User.objects.get(id=request.session['user_id'])
    posts = Post.objects.filter(user=user).order_by('-created_at')
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.user = user
        post.save()
        messages.success(request, "Post created!")
        return redirect('dashboard')
    return render(request, 'users/dashboard.html', {
        'user': user,
        'posts': posts,
        'form': form,
    })


