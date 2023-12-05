from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = RichTextField()
    conteudo = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    dataDeCriacao = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.titulo
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()