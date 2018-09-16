import asyncio
from balebot.filters import DefaultFilter
from balebot.models.messages import TextMessage
from balebot.updater import Updater
from balebot.utils.logger import Logger
from main_config import Config
from message import LogMessage

updater = Updater(token=Config.bot_token, loop=asyncio.get_event_loop())
dispatcher = updater.dispatcher
my_logger = Logger.get_logger()


def success_send_message(response, user_data):
    kwargs = user_data['kwargs']
    update = kwargs["update"]
    user_peer = update.get_effective_user()
    my_logger.info(LogMessage.success_send_message, extra={"user_id": user_peer.peer_id, "tag": "info"})


def failure_send_message(response, user_data):
    kwargs = user_data['kwargs']
    bot = kwargs["bot"]
    message = kwargs["message"]
    update = kwargs["update"]
    try_times = kwargs["try_times"]
    if try_times < Config.max_total_send_failure:
        try_times += 1
        user_peer = update.get_effective_user()
        my_logger.error(LogMessage.fail_send_message, extra={"user_id": user_peer.peer_id, "tag": "error"})
        kwargs = {"message": message, "update": update, "bot": bot, "try_times": try_times}
        bot.respond(update=update, message=message, success_callback=success_send_message,
                    failure_callback=failure_send_message, kwargs=kwargs)
    else:
        my_logger.error(LogMessage.max_fail_retried, extra={"tag": "error"})


@dispatcher.message_handler(filters=[DefaultFilter()])
def start_conversation(bot, update):
    user_peer = update.get_effective_user()
    text_message = TextMessage(Config.main_text_message)
    kwargs = {"message": text_message, "update": update, "bot": bot, "try_times": 1}
    bot.send_message(text_message, user_peer, success_callback=failure_send_message,
                     failure_callback=failure_send_message, kwargs=kwargs)
    dispatcher.finish_conversation(update)


updater.run()
