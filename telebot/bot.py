# Підключення бібліотек і файлів
from aiogram import executor
from dispatcher import dp
import handlers


# Підключення БД, та ініціалізація з'єднання
from db import BotDB
BotDB = BotDB('db.db')

# Запуск long polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
