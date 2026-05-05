from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


class DeletePreviousMessageMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        state: FSMContext = data.get("state")

        if state:
            user_data = await state.get_data()
            last_message_id = user_data.get("last_message_id")

            if last_message_id:
                try:
                    await event.bot.delete_message(
                        chat_id=event.chat.id,
                        message_id=last_message_id
                    )
                except Exception:
                    pass

        return await handler(event, data)