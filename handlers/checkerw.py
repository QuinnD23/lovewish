from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import OtmenaMark, WhatDoMark


@dp.message_handler(state=StateMachine.AcceptCommand)
async def command_start(message: Message):
    if message.text == "Подтвердить✅":
        await message.answer("Напишите номер желания: ", reply_markup=OtmenaMark)
        await StateMachine.AcceptNum.set()
    if message.text == "Отклонить❌":
        await message.answer("Напишите номер желания: ", reply_markup=OtmenaMark)
        await StateMachine.DislineNum.set()
    if message.text == "Назад◀️":
        await message.answer("Возвращаю...", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()


@dp.message_handler(state=StateMachine.AcceptNum)
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
            index = str(num) + "#" + username
            check2 = 1
            try:
                select_db("spisok", "id", "price", index)
            except:
                check2 = 0
                await message.answer("Неверно введен номер❌")
            if check2 == 1:
                money_award = select_db("spisok", "id", "price", index)
                now_money = select_db("info", "my_name", "money", lover)
                now_money += money_award
                update_db("info", "my_name", "money", lover, now_money)
                delete_db("spisok", "id", index)
                await message.answer("Желание подтверждено✅", reply_markup=WhatDoMark)
                await StateMachine.WhatDoTime.set()


@dp.message_handler(state=StateMachine.DislineNum)
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
            index = str(num) + "#" + username
            new_index = str(num) + "$" + username
            check2 = 1
            try:
                select_db("spisok", "id", "price", index)
            except:
                check2 = 0
                await message.answer("Неверно введен номер❌")
            if check2 == 1:
                update_db("spisok", "id", "id", index, new_index)
                await message.answer("Желание отклонено❌", reply_markup=WhatDoMark)
                await StateMachine.WhatDoTime.set()
