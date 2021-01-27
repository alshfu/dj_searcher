from django import forms
from scraping.Models.JobAD.JobTechTaxonomyItem import JobTechTaxonomyItem
from scraping.Models.location.City import City


class FinderForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects,
                                  widget=forms.Select(
                                      attrs={'class': 'form-control', 'onchange': ''}))
    branch = forms.ModelChoiceField(queryset=JobTechTaxonomyItem.objects,
                                    widget=forms.Select(
                                        attrs={'class': 'form-control', 'onchange': ''}))
