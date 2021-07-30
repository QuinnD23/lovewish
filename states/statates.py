from aiogram.dispatcher.filters.state import StatesGroup, State

class StateMachine(StatesGroup):
    LoverTime = State()
    LoverVerno = State()

    WhatDoTime = State()

    Wish = State()
    WishVerno = State()
    PriceWish = State()

    Options = State()

    MoneyVerno = State()
    MoneyWhat = State()
    MoneyPlus = State()
    MoneyMinus = State()

    MyWishCommand = State()
    MyWishNum = State()

    VipolnitCommand = State()
    VipolnitNum = State()

    AcceptCommand = State()
    AcceptNum = State()
    DislineNum = State()