from aiogram import Router
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove


router = Router()


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Выберите, что хотите заказать: "
             "блюда (/food) или напитки (/drinks).",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command(commands=["cancel"]))
@router.message(Text(text="отмена"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )
