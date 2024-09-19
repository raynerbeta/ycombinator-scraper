from django import forms


class FilterForm(forms.Form):
    """Form used for displaying filtering options."""

    FILTER_CHOICES = [
        ("", "No filter"),
        ("filter_1", "Filter 1 (>5 words, comments)"),
        ("filter_2", "Filter 2 (<=5 words, points)"),
    ]
    filter = forms.ChoiceField(
        choices=FILTER_CHOICES, required=False, label="Filter by"
    )
