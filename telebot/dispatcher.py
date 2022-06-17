# Підключення бібліотек і файлів
import config
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Вказуєм що данні будуть зберігатить в ОЗП
storage=MemoryStorage()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Виключення бота якщо не вказаний Api токен
if not config.BOT_TOKEN:
    exit("Токен не вказаний")

# Ініціалізація бота та диспетчерa, виділення памяті для FSM машини
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)

