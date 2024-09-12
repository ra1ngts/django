from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            for_title = 'Введите название продукта'
            for_description = 'Введите описание продукта'
            for_price = 'Укажите цену продукта'
            if name == 'title':
                field.widget.attrs.update({'placeholder': for_title})
            if name == 'description':
                field.widget.attrs.update({'placeholder': for_description})
            if name == 'price':
                field.widget.attrs.update({'placeholder': for_price})
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
                   'price': forms.TextInput(attrs={'class': 'form-control'})
                   }
