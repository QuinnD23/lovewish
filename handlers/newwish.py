from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import VernoMark, WhatDoMark, PriceMark


@dp.message_handler(state=StateMachine.Wish)
async def bot_message(message: Message):
    if message.text == "Назад◀️":
        await message.answer("Возвращаю...", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()
    else:
        username = message.from_user.username
        zhel = message.text
        index = select_db("info", "my_name", "index", username) + "$" + username
        try:
            insert_db("spisok", "id", index)
        except:
            update_db("spisok", "id", "zhel", index, zhel)

        update_db("spisok", "id", "my_name", index, username)
        update_db("spisok", "id", "zhel", index, zhel)

        await message.answer(f"Желание: {message.text}\n"
                             f"Верно?", reply_markup=VernoMark)
        await StateMachine.WishVerno.set()


@dp.message_handler(state=StateMachine.WishVerno)
async def bot_message(message: Message):
    if message.text == "Да✅":
        await message.answer("Укажите цену:", reply_markup=PriceMark)
        await StateMachine.PriceWish.set()
    if message.text == "Нет❌":
        await message.answer("Напишите желание:", reply_markup=ReplyKeyboardRemove())
        await StateMachine.Wish.set()

@dp.message_handler(state=StateMachine.PriceWish)
async def price_message(message: Message):
    username = message.from_user.username
    index = select_db("info", "my_name", "index", username) + "$" + username
    price = message.text
    if price == "10":
        update_db("spisok", "id", "price", index, price)
        await message.answer("Цена: 10")
    if price == "30":
        update_db("spisok", "id", "price", index, price)
        await message.answer("Цена: 30")
    if price == "50":
        update_db("spisok", "id", "price", index, price)
        await message.answer("Цена: 50")
    if price == "100":
        update_db("spisok", "id", "price", index, price)
        await message.answer("Цена: 100")
    if price == "250":
        update_db("spisok", "id", "price", index, price)
        await message.answer("Цена: 250")
    if price == "500":
        update_db("spisok", "id", "price", index, price)
        await message.answer("Цена: 500")
    if price == "Завершить✅":
        check_money_error = select_db("spisok", "id", "price", index)
        if check_money_error == 0:
            await message.answer("Вы не указали цену❌")
        else:
            index = select_db("info", "my_name", "index", username)
            index = str(int(index)+1)
            update_db("info", "my_name", "index", username, index)
            await message.answer("Желание успешно создано⚡️", reply_markup=WhatDoMark)
            await StateMachine.WhatDoTime.set()
