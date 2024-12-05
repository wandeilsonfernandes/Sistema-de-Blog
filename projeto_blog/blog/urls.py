from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # URLs do Blog
    path('post/novo/', views.criar_post, name='criar_post'),
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:pk>/', views.detalhe_post, name='detalhe_post'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:pk>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),
    path('post/<int:pk_post>/comentario/<int:pk_comentario>/remover/', views.remover_comentario, name='remover_comentario'),
    
    # URLs de Autenticação
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
