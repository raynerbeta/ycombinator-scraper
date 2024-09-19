# Web Scraper For [Hacker News](hacker_news)

## Overview
Coding exercise for Entry-Mid Level Software Developer - Stack Builders.

## Dependencies
- [Python (3.12)][python]
- pipenv (virtual environment)
- Django (web framework)
- pytest
- pytest-django
- pytest-sugar
- requests
- beautifulsoup4

## Features
- Web scraping
- Filtering and sorting:
  - **Filter 1:** filter all previous entries with more than five words in the title ordered by the number of comments first.
  - **Filter 2:** filter all previous entries with less than or equal to five words in the title ordered by points.


## Usage
> Note: **pipenv** is required for installing dependencies and running the app.
1. Install dependencies: `pipenv install`
2. Activate the virtual environment: `pipenv shell`
3. Change to the django project directory: `cd webapp/`
4. Migrate the database: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Run the app in your preferred web browser on the root path http://127.0.0.1:8000/

## License

Apache 2.0

[hacker_news]: <https://news.ycombinator.com/>
[python]: <https://www.python.org/>
