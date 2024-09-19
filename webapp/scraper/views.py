from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Entry
from .forms import FilterForm

URL = "https://news.ycombinator.com/"
DESIRED_ENTRIES = 30


def retrieve_entries(to_dict=False):
    while True:
        response = requests.get(URL)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        rows = soup.find_all("tr", class_="athing")
        entries = []
        for row in rows:
            number = row.find("span", class_="rank").text.replace(".", "").strip()
            td_title = row.find_all("td", class_="title")[1]
            title = td_title.find("a").text.strip()
            subtext = row.find_next_sibling("tr").find("td", class_="subtext")
            points = subtext.find("span", class_="score")
            if points:
                points = points.text.replace(" points", "").strip()
            else:
                points = 0
            comments = subtext.find_all("a")[-1].text.strip()
            if "comment" in comments:
                comments = comments.split()[0].replace("\xa0", "")
            else:
                comments = 0
            entry = Entry(number=number, title=title, points=points, comments=comments)
            entries.append(entry.to_dict() if to_dict else entry)
            if len(entries) == DESIRED_ENTRIES:
                return entries


def entries_view(request):
    session = request.session
    if "entries" not in session:
        session["entries"] = retrieve_entries(True)
        session.save()
    entries = [Entry.from_dict(entry) for entry in session["entries"]]
    form = FilterForm(request.GET)
    if form.is_valid():
        filter_by = form.cleaned_data.get("filter")
        if filter_by == "filter_1":
            entries = Entry.apply_filter_1(entries)
        elif filter_by == "filter_2":
            entries = Entry.apply_filter_2(entries)
    return render(request, "entries.html", {"entries": entries, "form": form})
