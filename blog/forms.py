from django.forms import ModelForm

from blog.models import Blog


class StyleFormsMixin:
    """
    Миксин для добавления стилей к полям формы.
    Применяет класс CSS "form-control" ко всем полям формы.
    Полю "is_published" присваивает класс "switch".
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализирует форму и применяет стили к полям.

        :param args: Дополнительные аргументы.
        :param kwargs: Дополнительные именованные аргументы.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if field_name == "is_published":
                field.widget.attrs["class"] = "switch"


class BlogForm(StyleFormsMixin, ModelForm):
    """
    Форма для создания новой статьи в блоге.
    Наследуется от ModelForm и использует StyleFormsMixin для стилизации полей.
    """
    class Meta:
        model = Blog
        fields = ("title", "text", "image")


class BlogUpdateForm(StyleFormsMixin, ModelForm):
    """
    Форма для редактирования существующей статьи в блоге.
    Наследуется от ModelForm и использует StyleFormsMixin для стилизации полей.
    """
    class Meta:
        model = Blog
        fields = ("title", "text", "image", "is_published")
