from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Artikel, Comment


class ArtikelForms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ('judul', 'body', 'kategory', 'img')
        widgets = {
            "judul" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'placeholder' : 'judul artikel', 
                    'required' : True
                }),
            "body" : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'cols' : '30',
                    'rows' : '10',
                    'required' : True
                }),
            "kategory" : forms.Select(
                attrs={
                    'class' : 'selectpicker',
                    'type' : 'text',
                    'required' : True,
                    'data-style' : 'btn-warning btn-outline',
                    'data-title' : 'Pilih Kategori',
                    'data-menu-style' : 'dropdown-blue',
                }),
            # "img" : forms.FileInput(
            #     attrs={
            #         'class' : 'figure-img img-fluid rounded',
            #         'type' : 'file',
            #         'required' : True
            #     }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nama', 'komen')
