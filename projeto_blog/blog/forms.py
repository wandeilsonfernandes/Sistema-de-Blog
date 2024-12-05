from django import forms
from .models import Post, Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']

        from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'categorias']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control'}),
            'categorias': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }