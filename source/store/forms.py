from django import forms
from django.forms import widgets
from webapp.models import StatusChoices


class ProductsListForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Title')
    description = forms.CharField(max_length=3000,
                                  required=False,
                                  label='Description',
                                  widget=widgets.Textarea(attrs={"cols": 50, "rows": 5}))
    image = forms.CharField(
        max_length=1000,
        required=True,
        label='Image')
    category = forms.ChoiceField(required=True, label='Category', choices=StatusChoices.choices)
    rest = forms.IntegerField(required=True, min_value=0, label='Rest')
    price = forms.DecimalField(required=True, max_digits=7, decimal_places=2, label='Price')


class ProductsSearchForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='')
