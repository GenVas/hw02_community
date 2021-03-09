"""yatube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # импорт правил из приложения posts
    path("", include("posts.urls")),
    # импорт правил из приложения admin
    path('admin/', admin.site.urls),
]
# "" — главная страница с лентой новых постов пользователей.
# "/<имя пользователя>" — страница с постами пользователя.
# Например, адресом личной страницы пользователя Лев Толстой (его логин — leo)
# будет /leo.
# "/<имя пользователя>/<pk поста>" — адрес страницы отдельного поста, где pk
# — идентификатор поста, первичный ключ записи в БД. В адресе мы «вкладываем»
# идентификатор поста в аккаунт автора. Страница с первой записью Льва будет
# иметь адрес /leo/1, а запись с pk=3, которую создал пользователь Антон,
# получит адрес /anton/3 Теперь по ссылке можно понять, какому автору
# принадлежит определённый пост. Это информативнее и удобнее, чем адреса
# вида /post/1 или post/3
# (хотя технически можно сделать и так).
