from aiogram import Router, F, Bot
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from keyboards.upload_cat_ikb import get_final_upload_ikb, get_cancel_ikb, UploadCallbackFactory, get_admin_ikb
from aiosqlite import Connection
from configs import config as cf
import pickle


router = Router()


class UploadCat(StatesGroup):
    uploading_cat = State()
    uploading_final = State()


@router.message(Command(commands=["upload"]))
async def upload_cat_cmd(message: Message, state: FSMContext):
    await message.answer(
        text='Отправьте фото и описание котейки',
    )
    await state.set_state(UploadCat.uploading_cat)


@router.message(
    UploadCat.uploading_cat,
    F.photo,
)
async def cat_uploaded_correctly(message: Message, state: FSMContext):
    '''
    Wait for user send photo and text.
    '''
    await state.update_data(cat_msg=message)
    await message.answer_photo(
        photo=message.photo[-1].file_id,
        caption=message.caption,
        reply_markup=get_final_upload_ikb()
    )
    await state.set_state(UploadCat.uploading_final)


@router.message(
    UploadCat.uploading_cat,
)
async def cat_uploaded_incorrectly(message: Message):
    '''
    User send wrong message.
    '''
    await message.answer(
        text='Похоже что вы ошиблись. Попробуйте еще раз.',
        reply_markup=get_cancel_ikb(),
    )


@router.callback_query(
    UploadCallbackFactory.filter(F.action=='cancel')
)
async def uploading_canceled(callback: CallbackQuery, state: FSMContext):
    '''
    User cancel the uploading.
    '''
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer(
        'Хорошо. Вы можете попробовать снова когда захотите.'
    )
    await state.clear()


@router.callback_query(
    UploadCallbackFactory.filter(F.action=='correctly'),
)
async def uploading_cunnectly(callback: CallbackQuery, state: FSMContext, bot: Bot):
    '''
    End FSM and send cat to moderating
    '''
    cat_msg = await state.get_data()
    cat_msg = cat_msg['cat_msg']
    await bot.send_message(
        chat_id=cf.ADMIN_CHAT_ID,
        text='НОВЫЙ КОТЕК!'
    )
    await bot.send_photo(
        chat_id=cf.ADMIN_CHAT_ID,
        caption=cat_msg.caption,
        photo=cat_msg.photo[-1].file_id,
        reply_markup=get_admin_ikb()
    )

    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer(
        text='Ура! Ваш котик на модерации.',
    )
    await state.clear()


@router.callback_query(
    UploadCallbackFactory.filter(F.action=='approved')
)
async def cat_approved(callback: CallbackQuery, db: Connection):
    '''
    Morerator approved a cat.
    '''
    await db.execute('INSERT INTO cats(cat_msg) VALUES (?)', (pickle.dumps(callback.message),))
    await db.commit()
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer(
        'Ура! у нас новый котейка.'
    )


@router.callback_query(
    UploadCallbackFactory.filter(F.action=='reject')
)
async def cat_reject(callback: CallbackQuery):
    '''
    Morerator reject a cat.
    '''
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer(
        'Туда его!'
    )
