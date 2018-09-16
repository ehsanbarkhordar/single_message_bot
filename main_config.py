import logging
import os

from message import ReadyMessage


class Config:
    request_timeout = int(os.environ.get('REQUEST_TIMEOUT', 5))
    # 0:print to output        1:use graylog       2:both 0 and 1
    source = os.environ.get('SOURCE', "bot_source")
    log_facility_name = os.environ.get('LOG_FACILITY_NAME', "python_bale_bot")
    real_time_fetch_updates = os.environ.get('REAL_TIME_FETCH_UPDATES', True)
    continue_last_processed_seq = os.environ.get('CONTINUE_LAST_PROCESSED_SEQ', False)
    max_total_send_failure = int(os.environ.get('MAX_TOTAL_FAILURE', 20))
    max_retries = int(os.environ.get('MAX_RETRIES', 1))
    check_interval = float(os.environ.get('CHECK_INTERVAL', 0.5))
    time_sleep = float(os.environ.get('TIME_SLEEP', 0.5))
    bot_token = os.environ.get('TOKEN', "1f9610ea2f56c115f880fc602a729ea09aecee53")
    bot_user_id = os.environ.get('BOT_USER_ID', "41")
    main_text_message = os.environ.get('MAIN_TEXT_MESSAGE', ReadyMessage.apology_message)
