# 🏥 SkyCare — Full-Stack Web Application

SkyCare — это полнофункциональное веб-приложение для работы с пользователями/пациентами, построенное на архитектуре **FastAPI + PostgreSQL + Static Frontend** и автоматически развернутое в облаке **Render**.

---

## 🚀 Деплой (Live Demos)

- **Frontend:** [https://skycare-frontend.onrender.com](https://skycare-frontend.onrender.com)
- **Backend API:** [https://skycare-backend.onrender.com](https://skycare-backend.onrender.com)
- **Swagger / OpenAPI Docs:** [https://skycare-backend.onrender.com/docs](https://skycare-backend.onrender.com/docs)

---

## 🛠️ Архитектура и стек технологий

### **Backend**
- **Python 3.14 / FastAPI** — высокопроизводительный асинхронный REST API фреймворк.
- **SQLAlchemy** — ORM для работы с базами данных и выполнения SQL-запросов.
- **Psycopg2 / Uvicorn** — драйвер БД и ASGI-сервер.
- **CORS Middleware** — разграничение доступа между фронтендом и бэкендом.

### **Database**
- **PostgreSQL (Render)** — облачная реляционная база данных.

### **Frontend**
- **HTML5 / CSS3 / JavaScript (ES6+)** — динамический клиент со встроенной валидацией и отправкой запросов через `fetch()`.

---

## 📡 Эндпоинты API (API Endpoints)

| Метод | Эндпоинт | Описание |
| :--- | :--- | :--- |
| `GET` | `/` | Проверка работоспособности сервиса |
| `GET` | `/health/db` | Проверка подключения бэкенда к PostgreSQL |
| `GET` | `/users` | Получение списка всех пользователей из БД |
| `POST` | `/users` | Создание нового пользователя (`name`, `email`) |

---

## 💻 Локальный запуск (Local Setup)

### 1. Клонирование репозитория
```bash
git clone [https://github.com/nezoxidc/SkyCare.git](https://github.com/nezoxidc/SkyCare.git)
cd SkyCare