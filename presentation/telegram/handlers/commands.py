from aiogram import Router
from aiogram.filters import CommandStart, Command
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

    text = f"Привет, я помогаю учить иностранные языки, давай скорее начинать"

    sent = await message.answer(text)

    await state.update_data(last_message_id=sent.message_id)

    return

@commands_router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
    """Обработчик для команды /help."""

    try:
        await message.delete()
    except Exception:
        pass

    # # 🔹 удаляем предыдущее help-сообщение
    # data = await state.get_data()
    # old_help_id = data.get("help_message_id")
    #
    # if old_help_id:
    #     try:
    #         await message.bot.delete_message(
    #             chat_id=message.chat.id,
    #             message_id=old_help_id
    #         )
    #     except Exception:
    #         pass

    text = (
        "📚 <b>Помощь по боту</b>\n\n"
        "Я помогу тебе учить язык в игровом формате:\n"
        "• тренировка слов\n"
        "• задания и челленджи\n"
        "• прокачка навыков\n\n"
        "Команды:\n"
        "/start — начать\n"
        "/help — показать это сообщение"
    )

    sent = await message.answer(text, parse_mode="HTML")

    # сохраняем id нового help-сообщения
    await state.update_data(last_message_id=sent.message_id)