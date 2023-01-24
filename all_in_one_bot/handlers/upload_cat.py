from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from keyboards.final_upload_ikb import get_final_upload_ikb, FinalUploadCallbackFactory
from aiosqlite import Connection
router = Router()


class UploadCat(StatesGroup):
    uploading_cat_photo = State()
    uploading_cat_name = State()
    uploading_cat_description = State()
    uploading_final = State()


@router.message(Command(commands=["upload"]))
async def upload_cat_cmd(message: Message, state: FSMContext):
    '''Start FSM'''
    await message.answer(
        text='Отправьте фото котейки',
    )
    await state.set_state(UploadCat.uploading_cat_photo)


@router.message(
    UploadCat.uploading_cat_photo,
    F.photo[-1].file_id.as_('cat_photo_id'),
)
async def cat_photo_correctly(message: Message, state: FSMContext, cat_photo_id: str):
    '''Good cat photo'''
    await state.update_data(cat_photo=cat_photo_id)
    await state.update_data(upload_by=message.from_user.id)
    await message.answer(
        text='Спасибо. Теперь скажите как его зовут.',
    )
    await state.set_state(UploadCat.uploading_cat_name)


@router.message(
    UploadCat.uploading_cat_photo,
)
async def cat_photo_incorrectly(message: Message):
    '''Bad cat photo'''
    await message.answer(
        text='Похоже что это не фото. Попробуйте еще раз.',
    )


@router.message(
    UploadCat.uploading_cat_name,
    F.text.as_('cat_name')
)
async def cat_name_correctly(message: Message, state: FSMContext, cat_name: str):
    '''Good cat name'''
    await state.update_data(cat_name=cat_name)
    await message.answer(
        text='Отлично, теперь введите описание котика.'
    )
    await state.set_state(UploadCat.uploading_cat_description)


@router.message(
    UploadCat.uploading_cat_name
)
async def cat_name_incorrectly(message: Message):
    '''Bad cat name'''
    await message.answer(
        text='Похоже что это не имя. Попробуйте еще раз.',
    )


@router.message(
    UploadCat.uploading_cat_description,
    F.text.as_('cat_description')
)
async def cat_desctiption_correctly(message: Message, state: FSMContext, cat_description: str):
    '''Good cat description'''
    await state.update_data(cat_description=cat_description)
    cat_data = await state.get_data()
    await message.answer_photo(
        photo=cat_data['cat_photo'],
        caption=f'Имя: {cat_data["cat_name"]}\n'
                f'Описание: {cat_data["cat_description"]}',
        reply_markup=get_final_upload_ikb()
    )
    await state.set_state(UploadCat.uploading_final)


@router.message(
    UploadCat.uploading_cat_description
)
async def cat_desctiption_incorrectly(message: Message):
    '''Bad cat description'''
    await message.answer(
        text='Похоже что это не описание котика. Попробуйте еще раз.',
    )


@router.callback_query(
    UploadCat.uploading_final,
    FinalUploadCallbackFactory.filter(F.action=='correctly'),
)
async def uploading_cunnently(callback: CallbackQuery, state: FSMContext, db: Connection):
    '''Good uploading'''
    cat_data = await state.get_data()
    await db.execute(
        '''
        INSERT INTO cats(image_id, upload_by, rating)
        VALUES(?, ?, ?)
        ''',
        (
            cat_data['cat_photo'],
            cat_data['upload_by'],
            0,
        ),
    )
    await db.commit()
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer(
        text='Ваш котик в надежных лапках',
    )
    await state.clear()


@router.callback_query(
    UploadCat.uploading_final,
    FinalUploadCallbackFactory.filter(F.action=='incorrectly')
)
async def uploading_incorrectly(callback: CallbackQuery, state: FSMContext):
    '''Bad uploading'''
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer(
        'Хорошо. Вы можете попробовать снова когда захотите.'
    )
    await state.clear()