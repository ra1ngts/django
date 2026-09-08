# :snake: Django Learning Projects

#### About project :
- __Django Learning Projects__ — a collection of educational projects developed while learning and practicing Django.
- The repository contains several independent projects created to explore different aspects of Django and web application development.

### :bride_with_veil: Wedding Salon

---

#### About project :
- __Wedding Salon__ — a personal Django-based e-commerce project developed for a real business use case.
- The website provides a catalog of wedding dresses and accessories with filtering, user interaction, reviews, and product sharing.

#### Features :
- Categories for wedding dresses and accessories.
- Create, edit, and delete products.
- Product filtering and search.
- Product reviews.
- Likes and dislikes.
- Social media sharing.
- User registration, authentication, and authorization.
- Multiple images for each product.
- Pagination.
- Logging.
- Caching.
- REST API integration.

#### Technologies and Libraries :
- Python 3.8.10
- Django 4.2
- Django REST Framework 3.14
- Django Allauth 0.54.0
- Django Filter 23.1
- Python-decouple 3.8
- Requests 2.28.2
- PostgreSQL
- HTML
- CSS

#### Website :
- [Wedding Salon](https://weddingh.pythonanywhere.com/dresses/)

#### Demonstration :
<img width="1920" height="1461" alt="w1" src="https://github.com/user-attachments/assets/bbe7ea74-e05b-4241-8dbe-1ed9c831c0d9" />
<img width="1920" height="1461" alt="w2" src="https://github.com/user-attachments/assets/35d5d1bc-68fb-436f-85bf-700bfae1de8b" />
<img width="1920" height="1461" alt="w3" src="https://github.com/user-attachments/assets/c87b4834-7cfa-409c-8d8d-70da6a9b822f" />

### :bride_with_veil: Wedding Salon (2.0)

---

#### About project :
- __Wedding Salon (2.0)__ — the second version of a personal Django-based project developed for a real business use case.
- The project introduces an updated technology stack, improved functionality, user interactions, and additional email and security features.

#### Features :
- Categories for wedding dresses and accessories.
- Create, edit, and delete dresses, accessories, and bride profiles.
- Product search and filtering.
- Reviews available to authorized users.
- Likes and dislikes for dresses and accessories.
- Social media sharing.
- User registration, authentication, and authorization.
- Multiple images for products.
- Pagination.
- Custom error handlers for 403, 404, and 500 errors.
- Email notifications for new reviews.
- Email notifications from the contact form.
- CAPTCHA protection for forms.

#### Technologies and Libraries :
- Python 3.12.3
- Django 5.0.6
- Django Allauth 0.63.3
- Django Filter 24.2
- Django Simple Captcha 0.6.0
- Python-decouple 3.8
- Bootstrap
- JavaScript
- HTML
- CSS

#### Website :
- [Wedding Salon (2.0)](https://weddh.pythonanywhere.com/dresses/)

#### Demonstration :
<img width="1920" height="1461" alt="w1" src="https://github.com/user-attachments/assets/c21bbee4-3c65-4c45-9fbd-53ff1ddc4a9c" />
<img width="1920" height="1461" alt="w2" src="https://github.com/user-attachments/assets/7d18b002-780a-47d6-ae5d-99c406f2f0aa" />
<img width="2736" height="2320" alt="w3" src="https://github.com/user-attachments/assets/dd4ff01d-b8b3-4563-b76e-b60dff1535c7" />

### :art: Art Gallery

---

#### About project :
- __Art Gallery__ — a personal project developed for my artist daughter.
- The website provides an online gallery for showcasing and managing artwork.
- The project was created as a personal birthday gift.

#### Features :
- Create, edit, and delete artwork.
- Create and manage artwork categories.
- Social media sharing.
- Responsive design for desktop and mobile devices.
- Contact form with email notifications.
- English and Russian localization with a language switcher.

#### Technologies and Libraries :
- Python 3.12.3
- Django 5.0.6
- Django Simple Captcha 0.6.0
- Django Modeltranslation 0.19.3
- Python-decouple 3.8
- Bootstrap
- JavaScript
- HTML
- CSS

#### Website :
- [Art Gallery](https://agataportfolio.pythonanywhere.com/)

#### Demonstration :
<img width="1920" height="1461" alt="gl1" src="https://github.com/user-attachments/assets/6f357fda-4c71-4a15-960d-e80f30c69e81" />
<img width="1920" height="1461" alt="gl2" src="https://github.com/user-attachments/assets/b9add434-aa9d-4132-9288-b78d656e2e30" />
<img width="1920" height="1461" alt="gl3" src="https://github.com/user-attachments/assets/200003dc-e9a4-4767-afd5-83f545cf4157" />
<img width="1920" height="1461" alt="gl4" src="https://github.com/user-attachments/assets/7fdab20b-7375-4fd3-b26f-01e16c438889" />
<img width="2736" height="2320" alt="gl5" src="https://github.com/user-attachments/assets/6f3a9d29-29d7-435d-8050-d06838b2cf7b" />

### :mountain_snow: Pereval REST API

---

#### About project :
- __Pereval REST API__ — an educational REST API project developed for the Federation of Sports Tourism of Russia (FSTR).
- The API is designed to collect and manage information about mountain passes submitted by tourists through a mobile application.

#### Features :
- Create and retrieve mountain pass records.
- Retrieve a specific pass by ID.
- Edit submitted data using partial updates.
- Validation of required fields and submitted data.
- User and contact information management.
- Mountain pass coordinates, elevation, difficulty level, and descriptions.
- Multiple images for each mountain pass.
- Moderation status tracking.
- Editing restrictions based on moderation status.
- Filtering and retrieving passes submitted by a specific user.
- Nested data serialization and writable nested relationships.
- Swagger API documentation.

#### API :
- `POST /api/v1/submitData/` — create a new mountain pass record.
- `GET /api/v1/submitData/` — retrieve submitted records.
- `GET /api/v1/submitData/?user__email=<email>` — retrieve records submitted by a specific user.
- `GET /api/v1/submitData/<id>/` — retrieve a specific record.
- `PATCH /api/v1/submitData/<id>/` — partially update a record.

#### Technologies and Libraries :
- Python 3.8.10
- Django 4.2
- Django REST Framework 3.14.0
- Django Filter 23.1
- drf-writable-nested 0.7.0
- drf-yasg 1.21.7
- Python-decouple 3.8
- Requests 2.28.2

#### API Documentation :
- [Swagger API Documentation](https://pereval.pythonanywhere.com/swagger/)

#### Demonstration :
<img width="1445" height="695" alt="Pereval_fstr_scr_1" src="https://github.com/user-attachments/assets/c048f83c-c352-4b3c-8056-589a479dc390" />
<img width="1445" height="695" alt="Pereval_fstr_scr_2" src="https://github.com/user-attachments/assets/d8812677-dea4-468b-8812-82d93a4b7d0e" />
<img width="1445" height="695" alt="Pereval_fstr_scr_3" src="https://github.com/user-attachments/assets/9bd7afe8-d3fd-497e-9f64-a542dac5a42f" />
<img width="1445" height="695" alt="Pereval_fstr_scr_4" src="https://github.com/user-attachments/assets/54d1b825-67ef-4b6e-81e0-5b80f9e434c9" />

### :nail_care: Manicure REST API

---

#### About project :
- __Manicure REST API__ — an educational REST API project for managing beauty salon appointments.
- The API allows clients to create, view, and cancel appointments through a mobile application.

#### Features :
- Create an appointment at a beauty salon.
- Select a salon, service, and master.
- Store client contact information and appointment date.
- Retrieve appointment information.
- Cancel an existing appointment.
- User registration and authentication.

#### API :
- `POST /api/v1/user-records/` — create a new appointment.
- `GET /api/v1/user-records/` — retrieve appointments.
- `GET /api/v1/user-records/<id>/` — retrieve a specific appointment.
- `DELETE /api/v1/user-records/<id>/` — cancel an appointment.

#### Technologies and Libraries :
- Python 3.8.10
- Django 4.2
- Django REST Framework 3.14.0
- Djoser 2.2.0
- Python-decouple 3.8
- Requests 2.28.2

#### Demonstration :
<img width="1445" height="695" alt="Manicure_scr_1" src="https://github.com/user-attachments/assets/4696d509-8c0a-453e-9630-0e85f90261a5" />
<img width="1445" height="695" alt="Manicure_scr_2" src="https://github.com/user-attachments/assets/cdb9753f-99c2-4acc-9136-4311aa5c12c3" />
<img width="1445" height="695" alt="Manicure_scr_3" src="https://github.com/user-attachments/assets/58992341-b2e7-4797-b02d-2e2179c469e9" />

### :newspaper: News Portal

---

#### About project :
- __News Portal__ — an educational Django project developed to practice building a full-featured web application.
- The project includes user authentication, news management, subscriptions, search, filtering, notifications, localization, and REST API functionality.

#### Features :
- User registration, authentication, and authorization, including Google authentication.
- Create, edit, and delete articles and news.
- News categories and category subscriptions.
- Likes and dislikes for posts.
- Search and filtering.
- Email notifications and weekly newsletters.
- Automatic user assignment to categories.
- Template and section caching.
- Error logging.
- Localization and internationalization.
- Light and dark themes.
- REST API integration.

#### Technologies and Libraries :
- Python 3.8.10
- Django 4.2
- Django REST Framework 3.14
- Django Allauth 0.54.0
- Django Filter 23.1
- Djoser 2.2.0
- Celery 5.2.7
- Redis 4.5.4
- APScheduler 3.10.1
- PostgreSQL
- Python-decouple 3.8
- Requests 2.28.2

#### Demonstration :
<img width="1443" height="851" alt="News_portal_scr_1" src="https://github.com/user-attachments/assets/c8013dc5-0db8-42a2-8c34-266a61bd043c" />
<img width="1443" height="851" alt="News_portal_scr_2" src="https://github.com/user-attachments/assets/a64a8a81-614f-4afd-b374-13d8a4185185" />
<img width="1443" height="851" alt="News_portal_scr_3" src="https://github.com/user-attachments/assets/58ca9376-18f6-4267-ad3f-7ce90398dcf8" />
<img width="1443" height="851" alt="News_portal_scr_4" src="https://github.com/user-attachments/assets/de7115d5-2c80-4408-9bfb-fd1ea08af8b5" />
<img width="1443" height="718" alt="News_portal_scr_5" src="https://github.com/user-attachments/assets/d9f5e97c-9c16-4ae9-89e5-11ffd1ccc296" />
<img width="1443" height="718" alt="News_portal_scr_6" src="https://github.com/user-attachments/assets/722fdecb-99d9-48f0-8ed6-4aa65ddd7ced" />

### :open_book: Bulletin Board

---

#### About project :
- __Bulletin Board__ — a final educational project developed while learning Django.
- The project is a web application for creating, managing, searching, and commenting on user-generated advertisements.

#### Features :
- Create advertisements by category.
- Edit, delete, and comment on advertisements.
- Search and filter advertisements.
- WYSIWYG editor for formatting text and managing images.
- User registration, authentication, and authorization.
- Personal user account for managing advertisements.
- Pagination.
- Email notifications using Celery.

#### Technologies and Libraries :
- Python 3.8.10
- Django 4.2
- Celery 5.2.7
- Django Allauth 0.54.0
- Django Filter 23.1
- Django CKEditor 6.6.1
- Python-decouple 3.8
- Requests 2.28.2
- HTML
- CSS

#### Demonstration :
<img width="1445" height="695" alt="Bulletin_board_scr_1" src="https://github.com/user-attachments/assets/18c7b1c0-51fb-40e8-8b97-023cc6de047b" />
<img width="1445" height="695" alt="Bulletin_board_scr_2" src="https://github.com/user-attachments/assets/cfdd53d8-afac-459d-9910-ed1bd48af075" />
<img width="1445" height="695" alt="Bulletin_board_scr_3" src="https://github.com/user-attachments/assets/ff344986-db50-49a4-a2c1-d3408bf35807" />
<img width="1445" height="695" alt="Bulletin_board_scr_4" src="https://github.com/user-attachments/assets/9329c9f1-20ca-472a-aa52-3a4db2ff4a6a" />
<img width="1445" height="695" alt="Bulletin_board_scr_6" src="https://github.com/user-attachments/assets/1292ab55-8ef8-46f5-a154-87b97e7c9d50" />
<img width="1445" height="695" alt="Bulletin_board_scr_7" src="https://github.com/user-attachments/assets/45f9e894-fd5b-42b3-8915-74b63feaa925" />
