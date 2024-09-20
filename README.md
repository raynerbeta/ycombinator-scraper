# Web Scraper for [Hacker News][hacker_news]

## Overview
Coding exercise for Entry-Mid Level Software Developer role at Stack Builders.

## Features
- Uses [Python][python] and [Django (web framework)][django]
- Web scraping for the news site [Hacker News][hacker_news]
- Retrieval of the first 30 news
- Filtering and sorting:
  - **Filter 1:** filter all previous entries with more than five words in the title ordered by the number of comments first.
  - **Filter 2:** filter all previous entries with less than or equal to five words in the title ordered by points.
> **Note:** sorting operations are made ascendently.

## Folder structure
- webapp (django project root folder)
    - webapp (django project subfolder)
    - scraper (django app folder)

## Dependencies
- [Python (3.12)][python]
- [pipenv (virtual environment)][pipenv]
- [Django (web framework)][django]
- [pytest][pytest]
- [pytest-django][pytest-django]
- [pytest-sugar][pytest-sugar]
- [pytest-cov][pytest-cov]
- [requests][requests]
- [beautifulsoup4][beautifulsoup4]

## Testing
The project was built applying TDD (Test Driven Development), therefore has test cases to check the correctness of the code. Additionally, the framework **pytest** (in addition with 3 plugins) was used to simplify the testing process.

For executing all test cases only one command is needed:
```bash
pytest
```
> **Note:** if the you aren't inside the virtual environment (but it's created), the following command can be run instead. Make sure you're under the django project root folder **webapp**.
> ```bash
> pipenv run pytest
> ```

## How to Run
> **Note:** a global installation of **pipenv** is required for installing dependencies and then running the app. If not installed, use the following command:
> ```bash
> pip install pipenv
> ```
For running the app just execute the next commands:
```bash
# Install dependencies
pipenv install --dev
# Activate the virtual environment
pipenv shell
# Change to the django project root folder
cd webapp/
# Run test cases and check all pass
pytest
# Migrate the database
python manage.py migrate
# Start the development server
python manage.py runserver
```
Finally, open the app in your preferred web browser on the root path http://127.0.0.1:8000/

## License

Apache 2.0

[hacker_news]: <https://news.ycombinator.com/>
[python]: <https://www.python.org/>
[django]: <https://www.djangoproject.com/>
[pipenv]: <https://pipenv-es.readthedocs.io/>
[pytest]: <https://docs.pytest.org/>
[pytest-django]: <https://pytest-django.readthedocs.io/>
[pytest-sugar]: <https://pypi.org/project/pytest-sugar/>
[pytest-cov]: <https://pytest-cov.readthedocs.io/>
[requests]: <https://pypi.org/project/requests/>
[beautifulsoup4]: <https://pypi.org/project/beautifulsoup4/>
