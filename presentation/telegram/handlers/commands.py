from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

commands_router = Router()


@commands_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """Обработчик для команды /start."""

    # удаляем сообщение пользователя (/start)
    try:
        await message.delete()
    except Exception:
        pass

    text = f"Привет"

    sent = await message.answer(
        text,
    )

    await state.update_data(start_message_id=sent.message_id)

    return
