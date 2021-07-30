from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import PriceMark, WhatDoMark, PlusMinusMark


@dp.message_handler(state=StateMachine.MoneyVerno)
async def command_start(message: Message):
    if message.text == "Да✅":
        check1 = 1
        username = message.from_user.username
        lover = select_db("info", "my_name", "lover", username)
        try:
            select_db("info", "my_name", "money", lover)
        except:
            await message.answer("Ваша вторая половинка не зарегистрирована😕", reply_markup=WhatDoMark)
            await StateMachine.WhatDoTime.set()
            check1 = 0
        if check1 == 1:
            checklover = select_db("info", "my_name", "lover", lover)
            if username == checklover:
                balance = select_db("info", "my_name", "money", lover)
                await message.answer(f"Текущий баланс @{lover} : {balance}", reply_markup=PlusMinusMark)
                await StateMachine.MoneyWhat.set()
            else:
                await message.answer("Ваша вторая половинка не указала вас😕", reply_markup=WhatDoMark)
                await StateMachine.WhatDoTime.set()
    if message.text == "Нет❌":
        await message.answer("Возвращаю...", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()


@dp.message_handler(state=StateMachine.MoneyWhat)
async def price_message(message: Message):
    if message.text == "Назад◀️":
        await message.answer("Возвращаю...", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()
    if message.text == "Увеличить✅":
        await message.answer("Укажите сумму, которую хотите добавить:", reply_markup=PriceMark)
        await StateMachine.MoneyPlus.set()
    if message.text == "Уменьшить❌":
        await message.answer("Укажите сумму, которую хотите вычесть:", reply_markup=PriceMark)
        await StateMachine.MoneyMinus.set()


@dp.message_handler(state=StateMachine.MoneyPlus)
async def price_message(message: Message):
    username = message.from_user.username
    lover = select_db("info", "my_name", "lover", username)
    price = message.text
    if price == "10":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 10")
    if price == "30":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 30")
    if price == "50":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 50")
    if price == "100":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 100")
    if price == "250":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 250")
    if price == "500":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 500")
    if price == "Завершить✅":
        check_money_error = select_db("info", "my_name", "money_plus", lover)
        if check_money_error == 0:
            await message.answer("Вы не указали сумму❌")
        else:
            new_balance = select_db("info", "my_name", "money", lover) + check_money_error
            update_db("info", "my_name", "money", lover, new_balance)
            update_db("info", "my_name", "money_plus", lover, 0)
            await message.answer(f"Баланс успешно обновлен⚡️\n"
                                 f"Новый баланс @{lover} : {new_balance}", reply_markup=WhatDoMark)
            await StateMachine.WhatDoTime.set()


@dp.message_handler(state=StateMachine.MoneyMinus)
async def price_message(message: Message):
    username = message.from_user.username
    lover = select_db("info", "my_name", "lover", username)
    price = message.text
    if price == "10":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 10")
    if price == "30":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 30")
    if price == "50":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 50")
    if price == "100":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 100")
    if price == "250":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 250")
    if price == "500":
        update_db("info", "my_name", "money_plus", lover, price)
        await message.answer("Сумма: 500")
    if price == "Завершить✅":
        check_money_error = select_db("info", "my_name", "money_plus", lover)
        if check_money_error == 0:
            await message.answer("Вы не указали сумму❌")
        else:
            new_balance = select_db("info", "my_name", "money", lover) - check_money_error
            update_db("info", "my_name", "money", lover, new_balance)
            update_db("info", "my_name", "money_plus", lover, 0)
            await message.answer(f"Баланс успешно обновлен⚡️\n"
                                 f"Новый баланс @{lover} : {new_balance}", reply_markup=WhatDoMark)
            await StateMachine.WhatDoTime.set()