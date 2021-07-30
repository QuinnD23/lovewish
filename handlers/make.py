from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import OtmenaMark, WhatDoMark


@dp.message_handler(state=StateMachine.VipolnitCommand)
async def command_start(message: Message):
    if message.text == "Отправить на проверку🔎":
        await message.answer("Напишите номер желания: ", reply_markup=OtmenaMark)
        await StateMachine.VipolnitNum.set()
    if message.text == "Назад◀️":
        await message.answer("Возвращаю...", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()


@dp.message_handler(state=StateMachine.VipolnitNum)
async def command_start(message: Message):
    if message.text == "Назад◀️":
        await message.answer("Возвращаю...", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()
    else:
        username = message.from_user.username
        lover = select_db("info", "my_name", "lover", username)
        check1 = 1
        try:
            num = int(message.text)
        except:
            check1 = 0
            await message.answer("Неверно введен номер❌")
        if check1 == 1:
            num = int(message.text) - 1
            index = str(num) + "$" + lover
            new_index = str(num) + "#" + lover
            check2 = 1
            try:
                select_db("spisok", "id", "price", index)
            except:
                check2 = 0
                await message.answer("Неверно введен номер❌")
            if check2 == 1:
                update_db("spisok", "id", "id", index, new_index)
                await message.answer("Желание отправлено на проверку✅", reply_markup=WhatDoMark)
                await StateMachine.WhatDoTime.set()
