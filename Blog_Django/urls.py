
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),    
    path('posts/<int:post_id>', views.post, name='post'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('adicionarComentario/<int:post_id>', views.adicionarComentario, name='adicionarComentario'),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
