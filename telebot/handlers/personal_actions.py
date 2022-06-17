# Підключення бібліотек і файлів
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

import re
import config
from bot import BotDB
from dispatcher import dp

# Створення класу для FSM машини
class FSM(StatesGroup):
    name = State()
    notise = State()
    value = State()

# Створення команди старт, яка записує данні юзера у БД
@dp.message_handler(commands = "start")
async def start(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)
    await message.bot.send_message(message.from_user.id, "Привіт!\nВведіть /help для отримання допомоги")

# Створення команди хелп, яка просто виводить текст з підсказкою
@dp.message_handler(commands = ("help"), commands_prefix = "/!")
async def help(message: types.Message):
    await message.reply("Команди для занесення витрат:\n"
                        "/spent /s !spent !s\n"
                        "Команди для отримання історії витрат:\n"
                        "/history /h !history !h\n"
                        "По дефолту історії відображається за весь час\n"
                        "Можна вказати додаткові параметри <i>all, day, week, month</i>\n"
                        )

# Початок діалогу з машиною, створення команди для записів про витрати
@dp.message_handler(commands = ("spent", "s"), commands_prefix = "/!")
async def cm_start(message: types.Message):
    await FSM.name.set()
    await message.reply("Вкажіть на що витратили кошти:\n /cancle для відміни")

# Створення команди яка в будь-який момент може зупинити FSM машину
@dp.message_handler(state="*", commands='/cancle')
@dp.message_handler(Text(equals='/cancle',ignore_case=True), state="*")
async def cancle(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("❌Відмінено")

# Записується перша відповідь від користувача і бот переводиться в режим очікування наступної відповіді від користувача
@dp.message_handler(state=FSM.name)
async def load_name(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    await message.reply("Вкажіть примітки:\n /cancle для відміни")
    await FSM.notise.set()

# Записується друга відповідь від користувача і бот переводиться в режим очікування наступної відповіді від користувача
@dp.message_handler(state=FSM.notise)
async def load_notise(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(notise=answer)
    await message.reply("Вкажіть скільки витратили:\n /cancle для відміни")
    await FSM.value.set()

# Записується остання відповідь від користувач, данні записуються у БД, FSM машина відключається
@dp.message_handler(state=FSM.value)
async def load_value(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(value=answer)
    data = await state.get_data()
    name = data.get('name')
    notise = data.get('notise')
    value = data.get('value')

    """Перевірка отриманної інформації від юзера, щоб з повідомлення вибрати тільки цифри і ","" перетворити в "." """
    x = re.findall(r"\d+(?:.\d+)?", value)
    if(len(x)):
        value = float(x[0].replace(',', '.'))
        BotDB.add_record(message.from_user.id, name, notise, value)
        await message.reply(f'{name} {notise} {value}\n'"✅Запис зроблено")
        await state.finish()
    else:
        await message.reply("❌Відмінено\nТреба ввести число😢")
        await state.finish()

# Створення команди яка в виводить історію витрат за певний період
@dp.message_handler(commands = ("history", "h"), commands_prefix = "/!")
async def start(message: types.Message):
    cmd_variants = ('/history', '/h', '!history', '!h')
    within_als = {
        "day": ('today', 'day', 'сьогодні', 'день'),
        "month": ('month', 'місяць'),
        "year": ('year', 'рік'),
        "week": ('week', 'тиждень'),
        "all": ('all', 'весь час'),
    }

    """Відкидання текстової частини команди яку прислав юзер, для збереження тільки  необхідних данних"""
    cmd = message.text
    for r in cmd_variants:
        cmd = cmd.replace(r, '').strip()

    """Вираз який буде по дефолту (історія за весь час)"""
    within = 'all'
    if(len(cmd)):
        for k in within_als:
            for als in within_als[k]:
                if(als == cmd):
                    within = k

    """Отримання даних з БД"""
    records = BotDB.get_records(message.from_user.id, within)

    """Виведення потрібних нам данних в месенджер"""
    if(len(records)):
        answer = f"🕘 Історія витрат за {within_als[within][-1]}\n\n"

        for r in records:
            answer += "<b>" + ("💵 Витрати") + "</b>"
            answer += f" - {r[2]}"
            answer += f" - {r[3]}"
            answer += f" <i><b>({r[4]}грн)</b></i>"
            answer += f" <i>({r[5]})</i>\n"

        await message.reply(answer)
    else:
        await message.reply("Записів не знайдено!")