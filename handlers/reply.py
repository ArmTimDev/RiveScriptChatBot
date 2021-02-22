from telegram.ext import MessageHandler, Filters
from helpers import reply as r


def reply(update, context):
    try:
        update.effective_message.reply_text(
            r(
                await message.reply_chat_action("typing")
                update.effective_message.text
            )
        )
    except:
        pass


__handlers__ = [
    [
        MessageHandler(
            Filters.text & Filters.reply,
            reply
        )
    ]
]
