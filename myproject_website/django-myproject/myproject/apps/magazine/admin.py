from django.contrib import admin
from django import forms 

from .models import NewsArticle

from .app_settings import ARTICLE_THEME_CHOICES

# Note that we could have defined the choices for.....
#  the theme field in models.py, but instead we created a custom ModelForm......
#   in administration and set the choices there. This
#  was done to avoid the creation of new database migrations whenever the ARTICLE_THEME_CHOICES is changed.

class NewsArticleModelForm(forms.ModelForm):
    theme = forms.ChoiceField(
        label=NewsArticle._meta.get_field('theme').verbose_name,
        choices=ARTICLE_THEME_CHOICES,
        required=not NewsArticle._meta.get_field('theme').blank,
        
        )
    class Meta:
        fields = "__all__"
