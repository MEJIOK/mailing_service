from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)

from blog.forms import BlogForm, BlogUpdateForm
from blog.models import Blog


class BlogList(ListView):
    """
    Представление для отображения списка всех статей.
    Наследуется от Django ListView.
    """
    model = Blog

    def get_context_data(self, *args, **kwargs):
        """
        Получает контекстные данные для отображения.
        Добавляет заголовок страницы "Список статей".

        :param args: Дополнительные аргументы.
        :param kwargs: Дополнительные именованные аргументы.
        :return: Словарь с контекстными данными.
        """
        context_data = super().get_context_data(*args, **kwargs)
        context_data["title"] = "Список статей"
        return context_data


class BlogCreate(LoginRequiredMixin, CreateView):
    """
    Представление для создания новой статьи.
    Требует авторизации пользователя.
    Наследуется от Django CreateView.
    """
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:list_blog")

    login_url = "users:login"
    redirect_field_name = "redirect_to"

    def get_context_data(self, **kwargs):
        """
        Получает контекстные данные для отображения.
        Добавляет заголовок страницы "Создание статьи".

        :param kwargs: Дополнительные именованные аргументы.
        :return: Словарь с контекстными данными.
        """
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Создание статьи"
        return context_data

    def form_valid(self, form):
        """
        Выполняет дополнительные действия, если форма заполнена правильно.
        Сохраняет статью и создает для неё slug.

        :param form: Заполненная форма.
        :return: Результат выполнения базового метода form_valid.
        """
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования существующей статьи.
    Требует авторизации и соответствующих прав.
    Наследуется от Django UpdateView.
    """
    model = Blog
    form_class = BlogUpdateForm
    success_url = reverse_lazy("blog:list_blog")
    permission_required = "update_blog"

    login_url = "users:login"
    redirect_field_name = "redirect_to"

    def get_context_data(self, **kwargs):
        """
        Получает контекстные данные для отображения.
        Добавляет заголовок страницы "Редактировать статью".

        :param kwargs: Дополнительные именованные аргументы.
        :return: Словарь с контекстными данными.
        """
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Редактировать статью"
        return context_data

    def form_valid(self, form):
        """
        Выполняет дополнительные действия, если форма заполнена правильно.
        Сохраняет отредактированную статью и обновляет slug.

        :param form: Заполненная форма.
        :return: Результат выполнения базового метода form_valid.
        """
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogDetail(DetailView):
    """
    Представление для отображения подробностей о статье.
    Наследуется от Django DetailView.
    """
    model = Blog
    fields = (
        "title",
        "text",
        "image",
    )
    success_url = reverse_lazy("blog:list_blog")

    def get_context_data(self, **kwargs):
        """
        Получает контекстные данные для отображения.
        Добавляет заголовок страницы "О статье".

        :param kwargs: Дополнительные именованные аргументы.
        :return: Словарь с контекстными данными.
        """
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "О статье"
        return context_data

    def get_object(self, queryset=None):
        """
        Получает объект статьи и увеличивает счетчик просмотров.

        :param queryset: Набор данных для получения объекта.
        :return: Объект статьи с увеличенным счетчиком просмотров.
        """
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления статьи.
    Требует авторизации и соответствующих прав.
    Наследуется от Django DeleteView.
    """
    model = Blog
    success_url = reverse_lazy("blog:list_blog")
    permission_required = "delete_blog"

    login_url = "users:login"
    redirect_field_name = "redirect_to"

    def get_context_data(self, **kwargs):
        """
        Получает контекстные данные для отображения.
        Добавляет заголовок страницы "Удалить статью".

        :param kwargs: Дополнительные именованные аргументы.
        :return: Словарь с контекстными данными.
        """
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Удалить статью"
        return context_data
