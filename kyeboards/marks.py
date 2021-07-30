from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

OtmenaMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад◀️"),
        ]
    ],
    resize_keyboard=True
)

WhatDoMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Загадать💫"),
            KeyboardButton(text="Выполнить😎"),

        ],
        [
            KeyboardButton(text="Мои желания🍀"),
            KeyboardButton(text="Изменить баланс💰"),

        ],
        [
            KeyboardButton(text="Подтвердить выполнение🔎"),

        ],
        [
            KeyboardButton(text="Узнать баланс🤑"),
            KeyboardButton(text="Настройки💞"),
        ]
    ],
    resize_keyboard=True
)

VernoMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да✅"),
            KeyboardButton(text="Нет❌"),
        ]
    ],
    resize_keyboard=True
)

AcceptMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Подтвердить✅"),
            KeyboardButton(text="Отклонить❌"),
            KeyboardButton(text="Назад◀️"),
        ]
    ],
    resize_keyboard=True
)

MyWishDoMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Удалить желание❌"),
            KeyboardButton(text="Назад◀️"),
        ]
    ],
    resize_keyboard=True
)

VipolnitMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить на проверку🔎"),
            KeyboardButton(text="Назад◀️"),
        ]
    ],
    resize_keyboard=True
)

PriceMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="10"),
            KeyboardButton(text="30"),
            KeyboardButton(text="50"),
        ],
        [
            KeyboardButton(text="100"),
            KeyboardButton(text="250"),
            KeyboardButton(text="500"),
        ],
        [
            KeyboardButton(text="Завершить✅"),
        ]
    ],
    resize_keyboard=True
)

PlusMinusMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Увеличить✅"),
            KeyboardButton(text="Уменьшить❌"),
            KeyboardButton(text="Назад◀️"),
        ],
    ],
    resize_keyboard=True
)
