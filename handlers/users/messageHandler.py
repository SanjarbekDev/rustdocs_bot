from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp,db 
from utils.parser import getURL

from data.config import ADMINS

@dp.message_handler(CommandStart(),user_id=ADMINS[0])
async def bot_start(message: types.Message):
    try:
        await db.add_user(full_name=message.from_user.full_name,username=message.from_user.username,telegram_id=message.from_user.id)
    except:
        pass
    users_c=await db.count_users()
    msg=f"Hello , {message.from_user.full_name}!\n"
    msg+="Search in inline mode 🔍\n\n"
    msg+=f"Users count: {users_c}"
    await message.answer(msg)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        await db.add_user(full_name=message.from_user.full_name,username=message.from_user.username,telegram_id=message.from_user.id)
    except:
        pass
    msg=f"Hello , {message.from_user.full_name}!\n"
    msg+="Search in inline mode 🔍"
    await message.answer(msg)

@dp.message_handler(commands="update")
async def bot_start(message: types.Message):
    try:
        await getURL(url="https://doc.rust-lang.org/book/")
    except Exception as e:
        await message.answer(text=f"Xatolik kuzatildi: {e}")
    await message.answer(f"Yangilandi!")
    
