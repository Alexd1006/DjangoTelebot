# DjangoTelebot

Telegram бот с Django API для регистрации пользователей.

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Настройка переменных окружения

1. Скопируйте файл с примером переменных окружения:
```bash
cp env_example .env
```

2. Отредактируйте `.env` и заполните свои данные:
```env
# Telegram Bot Token (получите у @BotFather)
BOT_TOKEN=YOUR_BOT_TOKEN_HERE

# Django Secret Key (сгенерируйте новый)
DJANGO_SECRET_KEY=YOUR_SECRET_KEY_HERE
```

### 3. Применение миграций

```bash
python manage.py migrate
```

### 4. Создание суперпользователя (опционально)

```bash
python manage.py createsuperuser
```

### 5. Запуск

В разных терминалах запустите:

**Django сервер:**
```bash
python manage.py runserver
```

**Telegram бот:**
```bash
python bot_main.py
```

## 📁 Структура проекта

```
DjangoTelebot/
├── bot/                    # Django приложение
│   ├── models.py          # Модели данных
│   ├── views.py           # API views
│   ├── serializers.py     # Сериализаторы
│   └── admin.py           # Админ панель
├── DjangoTelebot/         # Основные настройки Django
├── bot_main.py           # Telegram бот
├── .env                  # Переменные окружения (НЕ коммитить!)
├── env_example           # Пример переменных окружения
├── requirements.txt      # Зависимости
└── README.md            # Этот файл
```

## 🔧 Переменные окружения

### .env файл

```env
# Telegram Bot Token (получите у @BotFather)
BOT_TOKEN=YOUR_BOT_TOKEN_HERE

# Django Secret Key (сгенерируйте новый)
DJANGO_SECRET_KEY=YOUR_SECRET_KEY_HERE
```

## 📡 API Endpoints

- `POST /api/register` - Регистрация пользователя
  - Body: `{"user_id": 123456, "username": "user_name"}`
  - Response: `{"id": 1, "user_id": 123456, "username": "user_name", "created_at": "..."}`

## 🤖 Telegram Bot Commands

- `/start` - Зарегистрироваться в системе
- `/help` - Показать справку

## 🔒 Безопасность

- Файл `.env` добавлен в `.gitignore`
- Секретные ключи не хранятся в коде
- Используйте переменные окружения в production

## 🛠️ Разработка

### Создание нового бота

1. Напишите @BotFather в Telegram
2. Создайте нового бота: `/newbot`
3. Получите токен и добавьте в `.env`

### Генерация секретного ключа Django

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## 📝 Лицензия

MIT License 