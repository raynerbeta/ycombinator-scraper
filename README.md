# Web Scraper For [Hacker News][hacker_news]

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
- [requests][requests]
- [beautifulsoup4][beautifulsoup4]

## Testing
The project was built applying TDD (Test Driven Development), therefore has test cases to check the correctness of the code. Additionally, the framework **pytest** (in addition with 2 plugins) was used to simplify the testing process.

For executing all test cases only one command is needed:
```bash
pytest
```
> **Note:** if the virtual environment is not running, the following command can be run instead. Make sure you're under the django project root folder **webapp**.
> ```bash
> pipenv run pytest
> ```

## Usage
> **Note:** a global installation of **pipenv** is required for installing dependencies and then run the app. If not installed, use the following command:
> ```bash
> pip install pipenv
> ```
1. Install dependencies: `pipenv install`
1. Activate the virtual environment: `pipenv shell`
1. Change to the django project directory: `cd webapp/`
1. Run test cases and check all pass: `pytest`
1. Migrate the database: `python manage.py migrate`
1. Start the development server: `python manage.py runserver`
1. Open the app in your preferred web browser on the root path http://127.0.0.1:8000/

## License

Apache 2.0

[hacker_news]: <https://news.ycombinator.com/>
[python]: <https://www.python.org/>
[django]: <https://www.djangoproject.com/>
[pipenv]: <https://pipenv-es.readthedocs.io/>
[pytest]: <https://docs.pytest.org/>
[pytest-django]: <https://pytest-django.readthedocs.io/>
[pytest-sugar]: <https://pypi.org/project/pytest-sugar/>
[requests]: <https://pypi.org/project/requests/>
[beautifulsoup4]: <https://pypi.org/project/beautifulsoup4/>
