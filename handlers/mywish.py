from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import OtmenaMark, WhatDoMark


@dp.message_handler(state=StateMachine.MyWishCommand)
async def command_start(message: Message):
    if message.text == "Удалить желание❌":
        await message.answer("Напишите номер желания: ", reply_markup=OtmenaMark)
        await StateMachine.MyWishNum.set()
    if message.text == "Назад◀️":
        await message.answer("Возвращаю...", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()


@dp.message_handler(state=StateMachine.MyWishNum)
async def command_start(message: Message):
    if message.text == "Назад◀️":
        await message.answer("Возвращаю...", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()
    else:
        username = message.from_user.username
        check1 = 1
        try:
            num = int(message.text)
        except:
            check1 = 0
            await message.answer("Неверно введен номер❌")
        if check1 == 1:
            num = int(message.text) - 1
            index = str(num) + "$" + username
            check2 = 1
            try:
                select_db("spisok", "id", "price", index)
            except:
                check2 = 0
                await message.answer("Неверно введен номер❌")
            if check2 == 1:
                delete_db("spisok", "id", index)
                await message.answer("Желание успешно удалено🗑", reply_markup=WhatDoMark)
                await StateMachine.WhatDoTime.set()
