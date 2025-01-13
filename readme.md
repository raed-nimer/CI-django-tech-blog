# Introduction

### Project Goals

- To create a visually appealing website
- To create a website that is easy to navigate
- To create a website that is responsive across all devices
- To create a website that is interactive
- To create a website that is fun and easy to use

# User Stories

### First Time Visitor Goals

1. As a first time user, I want to be able to easily navigate the web app.
2. As a first time user, I want to be able to access the app on any device.
3. As a first time user, I want to be able to easily register for an account.
4. As a first time user, I want to be able to easily sign in and out of my account.
5. As a first time user, I want to be able to easily explore the recent blogs.
6. As a first time user, I want to be able to easily search for blogs.
7. As a first time user, I want to be able to contact the support.

### Authenticated User Goals

8. As an authenticated user, I want to be able to easily create blogs.
9. As an authenticated user, I want to be able to upload images with blogs.
10. As an authenticated user, I want to be able to edit my blogs.
11. As an authenticated user, I want to be able to delete my blogs.
12. As an authenticated user, I want to be able to comment on any blogs.

### Admin objectives

13. As an admin, I want to be able to log into the admin panel.
14. As an admin, I want to be able to easily manage blogs in case of an inappropriate content.
15. As an admin, I want to be able to provide an educational and interactive app.
16. As an admin, I want to be able to easily manage comments in case of an inappropriate content.
17. As an admin, I want to be able to easily manage user accounts.

## Database Schemas

![ER Diagram](media/images/readme_images/ER-diagram.png)

### User model

- The user model is the default Django user model.

| key          | Field Type    | Validation                  |
| ------------ | ------------- | --------------------------- |
| id           | IntegerField  |                             |
| password     | CharField     | max_length=128              |
| last_login   | DateTimeField |                             |
| is_superuser | BooleanField  |                             |
| username     | CharField     | max_length=150, unique=True |
| first_name   | CharField     | max_length=150, blank=True  |
| last_name    | CharField     | max_length=150, blank=True  |
| email        | EmailField    | max_length=254, unique=True |
| is_staff     | BooleanField  |                             |
| is_active    | BooleanField  |                             |
| date_joined  | DateTimeField |                             |

### Blog model

- The blog model is used to store all the blogs created by users.

| key         | Field Type      | Validation                                        |
| ----------- | --------------- | ------------------------------------------------- |
| id          | BigIntegerField | primary_key=True                                  |
| title       | CharField       | max_length=100                                    |
| description | RichTextField   |                                                   |
| image       | ImageField      | upload_to='images/', default='images/default.jpg' |
| user        | ForeignKey      | User, on_delete=models.CASCADE                    |
| category    | ForeignKey      | Category, on_delete=models.SET_NULL               |
| created_at  | DateTimeField   | auto_now_add=True                                 |
| updated_at  | DateTimeField   | auto_now=True                                     |

### Category model

- The category model is used to store categories of blogs.

| key        | Field Type      | Validation        |
| ---------- | --------------- | ----------------- |
| id         | BigIntegerField | primary_key=True  |
| name       | CharField       | max_length=200    |
| created_at | DateTimeField   | auto_now_add=True |
| updated_at | DateTimeField   | auto_now=True     |

### Comment model

- The comment model is used to store all the comments on the blogs.

| key        | Field Type      | Validation                                              |
| ---------- | --------------- | ------------------------------------------------------- |
| id         | BigIntegerField | primary_key=True                                        |
| user       | ForeignKey      | User, on_delete=models.CASCADE                          |
| blog       | ForeignKey      | Blog, related_name="comments", on_delete=models.CASCADE |
| name       | CharField       | max_length=200                                          |
| body       | TextField       |                                                         |
| created_at | DateTimeField   | auto_now_add=True                                       |
| updated_at | DateTimeField   | auto_now=True                                           |

### ContactFormResponse model

- The ContactFormResponse model is used to store all contect forms sent to support/developers from users.

| key         | Field Type      | Validation       |
| ----------- | --------------- | ---------------- |
| id          | BigIntegerField | primary_key=True |
| name        | CharField       | max_length=100   |
| email       | CharField       | max_length=100   |
| subject     | CharField       | max_length=100   |
| description | TextField       |                  |


### Languages and Frameworks

This project was created using the following languages and frameworks:

- [Django](https://www.djangoproject.com/) as the Python web framework.
- [Python](https://www.python.org/) as the backend programming language.
- [HTML](https://en.wikipedia.org/wiki/HTML) as the markup language and templating language.
- [CSS](https://en.wikipedia.org/wiki/CSS) as the style sheet language.
- [Bootstrap 5](https://getbootstrap.com/) as the CSS framework.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) to create carousel on index.html.

### Django Packages

| Packages                                   | Description (copied from the web)                                                                          |
| :----------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [Django](https://pypi.org/project/Django/) | Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. |
| [Pillow](https://pypi.org/project/Pillow/) | PIL is the Python Imaging Library.                                                                         |

### Other tools and programs

- [Visual Studio Code.](https://code.visualstudio.com/) Did all of my coding and synchronizing with GitHub on VS Code.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for hosting repositories.
- [Heroku](https://www.heroku.com/) where the website is deployed.
- [Grammarly](https://www.grammarly.com/) was used to double-check spelling mistakes.

# Features

### Home page

![Home page](/media/images/readme_images/home-page.jpeg)

### Contact page

![Contact page](/media/images/readme_images/contact-image.jpeg)

### About page

// Add about ss
// Add a heading for dashboard
// Attach Dashboard page
// Add heading for Profile Page
// Attach Image for profile page

### Login page

![Login page](/media/images/readme_images/login-image.jpeg)

### Register page

![register page](/media/images/readme_images/register-image.jpeg)

## Features to be implemented in future

- Give users an option to reply to a comment
- Give users an option to follow authors
- Give users an option to create a custom category
- Give users an option to search authors

# Testing

## Code Validation

### HTML Validation

### CSS Validtion

### Lighthouse Validation

### JavaScript Validation

### PEP8 Code Institute Python Linter Validation

## Manual testing
