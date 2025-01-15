# Introduction

In the dynamic world of technology and software development, sharing knowledge and staying updated is essential. Blogify stands as a premier platform designed specifically for tech enthusiasts and software developers, providing a space to create, manage, and share content that drives innovation and learning within the industry.

Blogify offers a user-friendly interface that simplifies the blogging experience, making it accessible to both beginners and seasoned professionals. Its intuitive design, combined with customizable templates and drag-and-drop features, ensures that users can produce high-quality blogs effortlessly. Tailored for the tech community, Blogify supports a wide range of content formats, allowing creators to share everything from detailed tutorials to industry insights in an engaging manner.

Beyond its technical features, Blogify fosters a vibrant community of tech professionals and enthusiasts. By encouraging collaboration and knowledge sharing, Blogify creates an environment where users can exchange ideas, learn from one another, and grow together. Regular webinars and support forums provide continuous learning opportunities, ensuring that users stay ahead in the fast-paced tech landscape.

More than just a blogging platform, Blogify is a comprehensive solution for transforming ideas into impactful content. Whether you’re sharing personal experiences, professional expertise, or exploring the latest tech trends, Blogify equips you with the tools to make your voice heard in the digital world. Join Blogify today and become a part of a community that’s shaping the future of technology.

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

## Agile development

Link to my [GitHub Agile Project](https://github.com/users/raed-nimer/projects/1)

I found this methodology a bit tricky when I started it, but eventually got a hang of it.
I found out about including agile development using kanban board after completing more than half of the project, so I decided to use the [Kanban](<https://en.wikipedia.org/wiki/Kanban_(development)>) and [MoSCoW](https://en.wikipedia.org/wiki/MoSCoW_method) prioritization method.

As a individual developer working on this project, I found creating "Epics" and "user stories" a bit time consuming.
However, I can see the benefits of using this methodology when working as a team. As of now, I will continue to use this method for all of my future projects and keep exploring more about it. I will also start looking into Jira, which is considered a good agile tool as well.

I created four columns: Todo, In Progress, Testing and Done.
I also created 9 labels:

- For MoSCoW prioritization: Must-have, Should-have, Could-have, Won't-have
- 5 helper labels: bug, Done, Epic, enhancement, User-story

I created 6 Epics divided into 13 user stories. Epics and user stories are connected with the # link on the title and in the description.

| Example    | Image                                                |
| ---------- | ---------------------------------------------------- |
| Epic       | ![Epic](media/images/readme_images/Epic-img.png)     |
| User story | ![User story](media/images/readme_images/US-img.png) |


### Languages and Frameworks

This project was created using the following languages and frameworks:

- [Django](https://www.djangoproject.com/) as the Python web framework.
- [Python](https://www.python.org/) as the backend programming language.
- [HTML](https://en.wikipedia.org/wiki/HTML) as the markup language and templating language.
- [CSS](https://en.wikipedia.org/wiki/CSS) as the style sheet language.
- [Bootstrap 5](https://getbootstrap.com/) as the CSS framework.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) to create carousel on index.html.

### Django Packages

| Packages                                                     | Description (copied from the web)                                                                                                                                                                                                                                              |
| :----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Django](https://pypi.org/project/Django/)                   | Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.                                                                                                                                                                     |
| [Pillow](https://pypi.org/project/Pillow/)                   | PIL is the Python Imaging Library.                                                                                                                                                                                                                                             |
| [whitenoise](https://pypi.org/project/whitenoise/)           | Radically simplified static file serving for Python web apps                                                                                                                                                                                                                   |
| [django-ckeditor](https://pypi.org/project/django-ckeditor/) | Django admin CKEditor integration.                                                                                                                                                                                                                                             |
| [gunicorn](https://pypi.org/project/gunicorn/)               | Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy. |
| [psycopg2](https://pypi.org/project/psycopg2/)               | Psycopg is the most popular PostgreSQL database adapter for the Python programming language.                                                                                                                                                                                   |
| [dj-database-url](https://pypi.org/project/dj-database-url/) | Use Database URLs in your Django Application.                                                                                                                                                                                                                                  |

### Other tools and programs

- [Visual Studio Code.](https://code.visualstudio.com/) Did all of my coding and synchronizing with GitHub on VS Code.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for hosting repositories.
- [Heroku](https://www.heroku.com/) where the website is deployed.
- [Grammarly](https://www.grammarly.com/) was used to double-check spelling mistakes.
- [Font Awesome](https://fontawesome.com/) was used for icons
- [Lucid](https://lucid.co/) was used to create database ERD

# Features

### Home page

- The home page is the first page that appears when a user visits the website.

- The page contains a welcome message, a hero image and recently added blogs.

![Home page](/media/images/readme_images/home-page.jpeg)

### Contact page

- Contact page can be used to contact support/developer

- The contact page consists of four inputs to fill out: Name, Email, Subject, and Description.

- If a user has any questions or concerns, they can go to the contact page, fill in their name, the email they wish to be contacted at, the subject of the matter, and then describe the matter in more detail in the description section for the support team.

![Contact page](/media/images/readme_images/contact-image.jpeg)

### About page

- The about page provides an overview of the website’s purpose and mission.

- It includes a brief history and summary of the core values.

- Visitors can learn more about the platform's goals and what sets it apart.

![About page](/media/images/readme_images/about-view.jpeg)

### Dashboard page

- The dashboard lets you create, view, edit, or delete your blogs.
  It provides an easy-to-use interface for managing your blogs, utilizing pagination.

![Dashboard page](media/images/readme_images/dashboard-view.jpeg)

### Profile page

- The profile page allows you to update your personal information, including your name, last name, username, and email.

- It provides a simple interface for managing your account details, ensuring your profile stays up-to-date.

![Profile page](media/images/readme_images/profile-view.jpeg)

### Login page

- Login page is where a registered user can login to their account.

- It has a form with the username and password fields.

![Login page](/media/images/readme_images/login-image.jpeg)

### Register page

- Register page is where a first time user can create their account.

- It has a form with the first name, last name, username, email, password and confirm password.

![register page](/media/images/readme_images/register-image.jpeg)

### Delete blog confirmation page

- Delete blog confirmation page is where the user can confirm if they want to delete the blog.

![delete blog confirmation page](/media/images/readme_images/delete-img.jpeg)

### Add blog page

- Add blog page is where the user can create a new blog.

- It has form with title, description, image and category fields.

![Add blog page](/media/images/readme_images/addblog-img.jpeg)

## Features to be implemented in future

- Give users an option to reply to a comment
- Give users an option to follow authors
- Give users an option to create a custom category
- Give users an option to search authors

# Testing

## Code Validation

### HTML Validation

- All pages were checked and passed through the official [W3C](https://validator.w3.org/nu/) validator.
- Validation was done on live app deployed on heroku.

| Page          | Validation image                                                                |
| ------------- | ------------------------------------------------------------------------------- |
| Home page     | ![Homepage-validation](media/images/readme_images/Homepage-html-validation.png) |
| About page    | ![About-validation](media/images/readme_images/aboutpage-html-validation.png)   |
| Contact page  | ![Contact-validation](media/images/readme_images/contactpage-validation.png)    |
| Register page | ![Register-validation](media/images/readme_images/registerpage-validation.png)  |
| Login page    | ![Login-validation](media/images/readme_images/loginpage-validation.png)        |
| Dasboard page | ![Dashboard-validation](media/images/readme_images/dashboard-validation.png)    |


### Lighthouse Validation

### JavaScript Validation

### PEP8 Code Institute Python Linter Validation

## Manual testing
