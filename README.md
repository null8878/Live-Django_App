# Live Django App

This repository contains a very small blogging application built with Django. It allows
users to create posts and now supports adding comments to each post.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install django
   ```
2. Apply migrations and start the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Visit `http://localhost:8000/` to access the blog.

## Features

- Create and view posts (authentication required to create posts).
- Add comments to posts.

This project is intentionally minimal, using default Django styling.
