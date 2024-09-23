# Use base image with Python 3.12
FROM mcr.microsoft.com/vscode/devcontainers/python:3.12

# Set working directory
WORKDIR /workspaces/ycombinator-scraper

# Install pipenv
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock, then run pipenv install
COPY Pipfile* ./
RUN pipenv install --dev

# Expose port 8000 for Django dev server
EXPOSE 8000
