import telebot
from telebot.types import Message
import requests
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

API_URL = "http://127.0.0.1:8000/api"

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения. Создайте файл .env")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    try:
        data = {
            "user_id": message.from_user.id, 
            "username": message.from_user.username
        }
        
        response = requests.post(API_URL + "/register", json=data)
        
        if response.status_code == 201:
            # Новый пользователь успешно зарегистрирован
            user_data = response.json()
            bot.send_message(
                message.chat.id, 
                f"✅ Вы успешно зарегистрированы!\nВаш уникальный номер: {user_data['id']}"
            )
        elif response.status_code == 200:
            # Пользователь уже существует
            user_data = response.json()
            bot.send_message(
                message.chat.id, 
                f"ℹ️ Вы уже были зарегистрированы ранее!\nВаш номер: {user_data['id']}"
            )
        else:
            # Ошибка сервера
            bot.send_message(
                message.chat.id, 
                f"❌ Произошла ошибка при регистрации! Статус: {response.status_code}"
            )
            print(f"Ошибка API: {response.status_code}")
            print(f"Ответ: {response.text}")
            
    except requests.exceptions.ConnectionError:
        bot.send_message(
            message.chat.id, 
            "❌ Не удалось подключиться к серверу. Попробуйте позже."
        )
        print("Ошибка подключения к API серверу")
    except Exception as e:
        bot.send_message(
            message.chat.id, 
            "❌ Произошла непредвиденная ошибка. Попробуйте позже."
        )
        print(f"Ошибка: {e}")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = """
🤖 Доступные команды:

/start - Зарегистрироваться в системе
/help - Показать это сообщение

Для получения дополнительной помощи обратитесь к администратору.
    """
    bot.send_message(message.chat.id, help_text)

if __name__ == "__main__":
    print("🤖 Telegram бот запущен...")
    print(f"📡 API URL: {API_URL}")
    print("💡 Используйте /start для регистрации")
    try:
        bot.polling(none_stop=True, interval=0)
    except KeyboardInterrupt:
        print("\n🛑 Бот остановлен пользователем")
    except Exception as e:
        print(f"❌ Ошибка запуска бота: {e}")