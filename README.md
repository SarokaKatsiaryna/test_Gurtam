# test_Gurtam

Gurtam Shortener is a web application for shortening long links.
Allows users to generate short URLs and administrators to manage links through the admin panel.

## 🚀 Functionality
✔️ Web interface for shortening links
✔️ Automatic generation of short links
✔️ Admin panel for managing links
✔️ Redirection by short links
✔️ Automatically remove links after expiration
✔️ Docker support for quick deployment

## 🛠 Technologies
- Backend: Python + Django
- Frontend: HTML + CSS
- Database: PostgreSQL
- Reverse Proxy: Nginx
- Deployment: Docker + Docker Compose

## Installation

### 🔹 1. Project cloning

``` bash
git clone https://github.com/SarokaKatsiaryna/test_Gurtam.git
cd test_Gurtam
```

Add files
.env
```bash
SECRET_KEY='django-insecure-fxdr+kddw7%$s#!ax)ww=gpn3#a$$rnf9&_4va-3ne8auz3igt'
DEBUG='True'
POSTGRES_DB="<you_name_database>"
POSTGRES_USER="<your username>"
POSTGRES_PASSWORD="<your password>"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"
```
docker/.env
```bash
SECRET_KEY='django-insecure-fxdr+kddw7%$s#!ax)ww=gpn3#a$$rnf9&_4va-3ne8auz3igt'
DEBUG='False'
POSTGRES_DB="<you_name_database>"
POSTGRES_USER="<your username>"
POSTGRES_PASSWORD="<your password>"
POSTGRES_HOST="postgres-db"
POSTGRES_PORT="5432"
DJANGO_SUPERUSER_USERNAME="<your username>"
DJANGO_SUPERUSER_EMAIL="<your email>"
DJANGO_SUPERUSER_PASSWORD="<your password>"
```

### 🔹 2. Launch via Docker

```bash
docker-compose up -d --build
```

After successful launch:
🔗 Web application is available at: http://localhost
🔑 Admin panel: http://localhost/admin

## 🎨 Web interface

The user interface (HTML + CSS) allows you to enter long links and get short ones.

📌 Example of use:
1. User goes to http://localhost
2. Enters a long link
3. Gets a short link

## 🔑 Admin Panel

Administrators can manage links via Django Admin:

📍 URL: http://localhost/admin
👤 Superuser login/password: set in .env file

## License

[MIT](https://choosealicense.com/licenses/mit/)
