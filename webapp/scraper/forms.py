from django import forms


class FilterForm(forms.Form):
    FILTER_CHOICES = [
        ("", "No filter"),
        ("filter_1", "Filter 1"),
        ("filter_2", "Filter 2"),
    ]
    filter = forms.ChoiceField(
        choices=FILTER_CHOICES, required=False, label="Filter by"
    )
