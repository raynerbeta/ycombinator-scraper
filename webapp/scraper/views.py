from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Entry
from .forms import FilterForm

URL = "https://news.ycombinator.com/"
DESIRED_ENTRIES = 30


def retrieve_entries(to_dict=False):
    """Function used to scrape news from specific URL."""
    # Condition specified for running indefinitely until return is reached
    while True:
        response = requests.get(URL)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        # Extract all table rows with class "athing"
        rows = soup.find_all("tr", class_="athing")
        entries = []
        for row in rows:
            # Retrieve the number from span with class "rank" and remove "."
            number = row.find("span", class_="rank").text.replace(".", "").strip()
            # Extract the second table data with class "title"
            td_title = row.find_all("td", class_="title")[1]
            # Retrieve the title from the first anchor tag
            title = td_title.find("a").text.strip()
            # Extract the next table row that contains relevant data
            # And also extract table data with class "subtext"
            subtext = row.find_next_sibling("tr").find("td", class_="subtext")
            # Retrieve points from span with class "score"
            points = subtext.find("span", class_="score")
            if points:
                points = points.text.replace(" points", "").strip()
            else:
                points = 0
            # Retrieve comments from the last anchor tag
            comments = subtext.find_all("a")[-1].text.strip()
            if "comment" in comments:
                # Remove character escape sequence
                comments = comments.split()[0].replace("\xa0", "")
            else:
                comments = 0
            # Create Entry object
            entry = Entry(number=number, title=title, points=points, comments=comments)
            entries.append(entry.to_dict() if to_dict else entry)
            # Return condition for stopping the external while
            if len(entries) == DESIRED_ENTRIES:
                return entries


def entries_view(request):
    """Function view for rendering the main page."""
    # Session storage is used for persisting the entries once retrieved
    session = request.session
    # Check if entries are already loaded in session
    if "entries" not in session:
        # If not, they're fetched and saved
        session["entries"] = retrieve_entries(True)
        session.save()
    # Load entries from session
    entries = [Entry.from_dict(entry) for entry in session["entries"]]
    # Load form
    form = FilterForm(request.GET)
    if form.is_valid():
        # Get the filter
        filter_by = form.cleaned_data.get("filter")
        # Apply filter according criterion
        if filter_by == "filter_1":
            entries = Entry.apply_filter_1(entries)
        elif filter_by == "filter_2":
            entries = Entry.apply_filter_2(entries)
    # Render the view with both: entries and form
    return render(request, "entries.html", {"entries": entries, "form": form})
