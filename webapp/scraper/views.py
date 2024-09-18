from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Entry
from .forms import FilterForm


def entries_view(request):
    if "entries" not in request.session:
        # Pending update of entries
        request.session["entries"] = []
    entries = request.session["entries"]
    form = FilterForm(request.GET)
    if form.is_valid():
        filter = form.cleaned_data.get("filter_by")
        # Pending filtering entries
        if filter == "filter_1":
            entries = []
        elif filter == "filter_2":
            entries = []
    return render(request, "entries.html", {"entries": entries, "form": form})
