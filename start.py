from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import OtmenaMark, WhatDoMark, VernoMark, MyWishDoMark, VipolnitMark, AcceptMark


@dp.message_handler(Command("start"))
async def command_start(message: Message):
    username = message.from_user.username
    try:
        insert_db("info", "my_name", username)
    except:
        pass
    await message.answer("**Инструкция для Бота Желаний**\n"
                         "✨Бот создан для влюбленных пар. Здесь вы сможете загадать или выполнить желание своей второй "
                         "половинки, а также придумать с ней приз, для которого вам пригодится баланс\n"
                         "📍Шаг 1\n"
                         "Вы и ваша вторая половинка должны указать друг друга (имя пользователя Телеграм через @)\n"
                         "📍Шаг 2\n"
                         "Ознакомьтесь с меню:\n"
                         "Загадать💫 - загадайте желание вашей второй половинке, а также установите сумму, которую она "
                         "получит за его выполнение\n"
                         "Исполнить😎 - узнайте, что желает ваша вторая половинка, исполните и отправьте на проверку\n"
                         "Мои желания🍀 - список ваших желаний, здесь вы сможете удалить желание\n"
                         "Изменить баланс💰 - увеличьте или уменьшите баланс второй половинки\n"
                         "Подтвердить выполнение🔎 - подтвердите, что вторая половинка исполнила ваше желание, после "
                         "подтверждения она получит вознаграждение на свой баланс\n"
                         "Узнать баланс🤑 - узнайте свой текущий баланс, а также баланс второй половинки\n"
                         "Настройки💞 - измените имя пользователя своей второй половинке, в случае изменения или ошибки "
                         "при регистрации\n")
    await message.answer(f"Привет, симпопулька - {username}")
    checklover = select_db("info", "my_name", "lover", username)
    if checklover == "0":
        await message.answer(f"Укажите вторую половинку\n"
                             f"Напишите Имя пользователя через @")
        await StateMachine.LoverTime.set()
    else:
        await message.answer(f"Чем займемся?", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()

# РЕГИСТРАЦИЯ


@dp.message_handler(state=StateMachine.LoverTime)
async def command_start(message: Message):
    await message.answer(f"Вашу вторую половинку зовут: {message.text}\n"
                         f"Верно?", reply_markup=VernoMark)
    username = message.from_user.username
    lovername = message.text[1:]
    update_db("info", "my_name", "lover", username, lovername)
    await StateMachine.LoverVerno.set()


@dp.message_handler(state=StateMachine.LoverVerno)
async def command_start(message: Message):
    if message.text == "Да✅":
        await message.answer(f"Поздравляю, вторая половинка установлена🥳\n"
                             f"Чем займемся?", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()
    if message.text == "Нет❌":
        await message.answer(f"Укажите вторую половинку\n"
                             f"Напишите Имя пользователя через @", reply_markup=ReplyKeyboardRemove())
        await StateMachine.LoverTime.set()

# РЕГИСТРАЦИЯ END


@dp.message_handler(state=StateMachine.WhatDoTime)
async def command_start(message: Message):
    username = message.from_user.username
    lover = select_db("info", "my_name", "lover", username)

    if message.text == "Загадать💫":
        await message.answer("Напишите желание:", reply_markup=OtmenaMark)
        await StateMachine.Wish.set()

    if message.text == "Выполнить😎":
        check1 = 1
        try:
            select_db("info", "my_name", "money", lover)
        except:
            await message.answer(f"Ваша вторая половинка не зарегистрирована😕")
            check1 = 0
        if check1 == 1:
            checklover = select_db("info", "my_name", "lover", lover)
            if username != checklover:
                await message.answer("Ваша вторая половинка не указала вас😕")
            else:
                await message.answer(f"@{lover} желает:", reply_markup=VipolnitMark)
                kolvo = int(select_db("info", "my_name", "index", lover))
                for i in range(kolvo):
                    index = str(i) + "$" + lover
                    try:
                        select_db("spisok", "id", "zhel", index)
                    except:
                        continue
                    wish_text = select_db("spisok", "id", "zhel", index)
                    wish_price = select_db("spisok", "id", "price", index)
                    text = str(i + 1) + f". {wish_text} - 💰{wish_price}"
                    await message.answer(text)
                await StateMachine.VipolnitCommand.set()

    if message.text == "Настройки💞":
        await message.answer("Вы хотите изменить вторую половинку?🤔", reply_markup=VernoMark)
        await StateMachine.Options.set()

    if message.text == "Изменить баланс💰":
        await message.answer(f"Вы хотите изменить баланс @{lover}?🤔", reply_markup=VernoMark)
        await StateMachine.MoneyVerno.set()

    if message.text == "Узнать баланс🤑":
        check1 = 1
        my_money = select_db("info", "my_name", "money", username)
        try:
            select_db("info", "my_name", "money", lover)
        except:
            await message.answer(f"Ваш баланс : {my_money}\n"
                                 f"Баланс @{lover} : Ваша вторая половинка не зарегистрирована😕")
            check1 = 0
        if check1 == 1:
            lover_money = select_db("info", "my_name", "money", lover)
            checklover = select_db("info", "my_name", "lover", lover)
            if username == checklover:
                await message.answer(f"Ваш баланс : {my_money}\n"
                                     f"Баланс @{lover} : {lover_money}")
            else:
                await message.answer(f"Ваш баланс : {my_money}\n"
                                     f"Баланс @{lover} : Ваша вторая половинка не указала вас😕")

    if message.text == "Мои желания🍀":
        await message.answer("Ваши желания:", reply_markup=MyWishDoMark)
        kolvo = int(select_db("info", "my_name", "index", username))
        for i in range(kolvo):
            index = str(i) + "$" + username
            try:
                select_db("spisok", "id", "zhel", index)
            except:
                continue
            wish_text = select_db("spisok", "id", "zhel", index)
            wish_price = select_db("spisok", "id", "price", index)
            text = str(i+1) + f". {wish_text} - 💰{wish_price}"
            await message.answer(text)
        await StateMachine.MyWishCommand.set()

    if message.text == "Подтвердить выполнение🔎":
        check1 = 1
        try:
            select_db("info", "my_name", "money", lover)
        except:
            await message.answer(f"Ваша вторая половинка не зарегистрирована😕")
            check1 = 0
        if check1 == 1:
            checklover = select_db("info", "my_name", "lover", lover)
            if username != checklover:
                await message.answer("Ваша вторая половинка не указала вас😕")
            else:
                await message.answer(f"Задания на проверке:", reply_markup=AcceptMark)
                kolvo = int(select_db("info", "my_name", "index", username))
                for i in range(kolvo):
                    index = str(i) + "#" + username
                    try:
                        select_db("spisok", "id", "zhel", index)
                    except:
                        continue
                    wish_text = select_db("spisok", "id", "zhel", index)
                    wish_price = select_db("spisok", "id", "price", index)
                    text = str(i + 1) + f". {wish_text} - 💰{wish_price}"
                    await message.answer(text)
                await StateMachine.AcceptCommand.set()


# НАСТРОЙКИ

@dp.message_handler(state=StateMachine.Options)
async def command_start(message: Message):
    if message.text == "Да✅":
        await message.answer(f"Укажите вторую половинку\n"
                             f"Напишите Имя пользователя через @", reply_markup=ReplyKeyboardRemove())
        await StateMachine.LoverTime.set()
    if message.text == "Нет❌":
        await message.answer("Возвращаю...", reply_markup=WhatDoMark)
        await StateMachine.WhatDoTime.set()


# НАСТРОЙКИ END
