import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

bot = Bot(token='7187578312:AAHdnJMPALYQv0e9dW0IaIXaFZV_5vcSTGw')
dp = Dispatcher()

CYRILLIC_TO_LATIN = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
    'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k',
    'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'ie', 'ы': 'y', 'ь': '',
    'э': 'e', 'ю': 'iu', 'я': 'ia',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts',
    'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': 'Ie', 'Ы': 'Y', 'Ь': '',
    'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia'
}

@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Введи ФИО на кириллице для транслитерации.'
    logging.info(f'{user_name} ({user_id}) запустил бота')
    await message.answer(text)

@dp.message()
async def send_echo(message: Message):
    text = message.text
    transliterated = [CYRILLIC_TO_LATIN.get(char, char) for char in text]
    result = ''.join(transliterated)
    
    logging.info(f"Transliterated: {text} -> {result}")
    await message.answer(f"Результат транслитерации:\n{result}")

if __name__ == '__main__':
    dp.run_polling(bot)
