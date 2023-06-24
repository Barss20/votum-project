import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from buttons import om1, gm1, bgm1
from config import TOKEN
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def is_admin(user_id):
    connection = sqlite3.connect('/home/ubuntu/pythonProject1/VotumNGO/db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT user_id FROM AdminTG_telegramadmin')
    results = cursor.fetchall()
    connection.close()
    user_ids = [result[0] for result in results]
    return user_id in user_ids


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if await is_admin(message.from_user.id):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(InlineKeyboardButton(text='Admin', callback_data='admin'))
        keyboard.row(InlineKeyboardButton(text="Головне меню", callback_data="bgm1"))
        await message.answer(
            "👋Привіт! Вас вітає ДОВІДНИК для ВПО з актуальних послуг у місті Одеса та Одеській області, я допоможу тобі "
            "знайти БЕЗКОШТОВНУ допомогу від держави та гуманітарних "
            "організацій."
            "\n\nЗВЕРТАЄМО УВАГУ, ЩО ЗАЛЕЖНО ВІД СИТУАЦІЇ, ІНФОРМАЦІЯ МОЖЕ ЗМІНЮВАТИСЬ!!! "
            "\nНатисніть ʼГоловне менюʼ щоб побачити бажану інформацію 👇", reply_markup=keyboard)

    else:
        await message.answer(
            "👋Привіт! Вас вітає ДОВІДНИК для ВПО з актуальних послуг у місті Одеса та Одеській області, я допоможу тобі "
            "знайти БЕЗКОШТОВНУ допомогу від держави та гуманітарних "
            "організацій."
            "\n\nЗВЕРТАЄМО УВАГУ, ЩО ЗАЛЕЖНО ВІД СИТУАЦІЇ, ІНФОРМАЦІЯ МОЖЕ ЗМІНЮВАТИСЬ!!! "
            "\nНатисніть ʼГоловне менюʼ щоб побачити бажану інформацію 👇", reply_markup=gm1)


@dp.callback_query_handler()
async def call_back_inline(call: types.CallbackQuery):
    connection = sqlite3.connect('/home/ubuntu/pythonProject1/VotumNGO/db.sqlite3')
    cursor = connection.cursor()
    if call.data == 'bgm1':
        await call.message.edit_text(text='Виберіть дію нижче👇', reply_markup=om1)
    if call.data == 'bom1':

        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 1')
        result = cursor.fetchone()



        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom2":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 2')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom3":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 3')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom4":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 4')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom5":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 5')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom6":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 6')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom7":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 7')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom8":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 8')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom9":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 9')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom10":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 10')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom11":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE title = 11')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom12":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 12')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom13":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 13')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom14":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 14')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom15":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 15')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom16":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 16')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "bom17":
        # Выполните запрос к базе данных
        cursor.execute('SELECT content FROM AdminTG_text WHERE id = 17')
        result = cursor.fetchone()  # Получите результат запроса

        # Проверьте, есть ли результат, и сохраните его в переменную long_text
        if result:
            long_text = result[0]
        else:
            long_text = "Значение не найдено"

        # Разделите long_text на части и отправьте каждую часть боту
        parts = [long_text[i:i + 4096] for i in range(0, len(long_text), 4096)]
        for part in parts:
            await call.message.edit_text(text=f"{part}", reply_markup=gm1)

    if call.data == "admin":
        keyboard = InlineKeyboardMarkup().add(bgm1)
        if await is_admin(call.from_user.id):

            admin_url = 'http://130.61.186.30/admin'

            await call.message.edit_text(f"Админка запущена!\nURL: {admin_url}", reply_markup=keyboard)

    cursor.close()
    connection.close()


@dp.message_handler(commands=['admin'])
async def process_start_command(message: types.Message):
    if await is_admin(message.from_user.id):
        admin_url = "http://130.61.186.30/admin"
        await message.answer(text=f"Админка доступна по адресу: \n{admin_url}")

@dp.message_handler(commands=['id'])
async def process_start_command(message: types.Message):
    await message.answer(text=f'{message.from_user.id}', reply_markup=gm1)

if __name__ == '__main__':
    executor.start_polling(dp)