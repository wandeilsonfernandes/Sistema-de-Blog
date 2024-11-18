from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comentario, Categoria
from .forms import PostForm, ComentarioForm

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts':posts})

def detalhe_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all()
    return render(request, 'blog/detalhe_post.html', {'post' : post, 'comentarios': comentarios})

@login_required
def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            form.save_m2m()  # Para categorias
            return redirect('detalhe_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/form_post.html', {'form': form})


@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.autor:
        return redirect('lista_posts')  # Somente o autor pode editar
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalhe_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/form_post.html', {'form': form})

@login_required
def adicionar_comentario(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect('detalhe_post', pk=post.pk)
    else:
        form = ComentarioForm()
    return render(request, 'blog/form_comentario.html', {'form': form})


@login_required
def remover_comentario(request, pk_comentario, pk_post):
    comentario = get_object_or_404(Comentario, pk=pk_comentario)
    post = get_object_or_404(Post, pk=pk_post)
    if request.user == post.autor or request.user == comentario.autor:
        comentario.delete()
    return redirect('detalhe_post', pk=post.pk)
