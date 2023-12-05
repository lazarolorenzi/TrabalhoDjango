from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comentario
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponse
from blog.forms import ComentarioForm
# Create your views here.
@login_required(login_url='/login/')
def home(request):
    posts = Post.objects.annotate(nComentarios=Count('comentario')).order_by('-nComentarios', 'dataDeCriacao')
    return render(request, 'home.html', {'posts': posts})
@login_required(login_url='/login/')
def post(request, post_id):
    post = Post.objects.get(pk = post_id)
    comentarios = Comentario.objects.filter(post=post)
    return render(request, 'post.html', {'post': post, 'comentarios': comentarios})
   

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username = name).first()

        if user: 
            error_message = 'Usuário já existe.'
            return render(request, 'cadastro.html', {'error_message': error_message})    
        user = User.objects.create_user(username=name, email=email, password=senha)
        user.save
        return redirect('login')
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        senha = request.POST.get('senha')
        user = authenticate(username=name, password=senha)
        if user:
            login_django(request, user)
            return redirect('home')
        else:
            error_message = 'Usuário ou senha inválidos. Por favor, tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})


@user_passes_test(lambda u: u.is_authenticated and u.is_staff)
def Botaodoadmin(request):
    return render(request, 'admin')


def adicionarComentario(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.post = post
            comentario.save()
            return redirect('post', post_id)

    else:
        form = ComentarioForm()

    return render(request, 'adicionarComentario.html', {'form': form, 'post': post})