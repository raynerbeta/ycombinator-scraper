# Use base image with Python 3.12
FROM mcr.microsoft.com/vscode/devcontainers/python:3.12
USER vscode
WORKDIR /workspaces/ycombinator-scraper
COPY Pipfile* ./
RUN pip install pipenv && pipenv install --dev
