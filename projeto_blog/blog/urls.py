from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:pk>/', views.detalhe_post, name='detalhe_post'),
    path('post/novo/', views.criar_post, name='criar_post'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:pk>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),
    path('post/<int:pk_post>/comentario/<int:pk_comentario>/remover/', views.remover_comentario, name='remover_comentario'),
]

