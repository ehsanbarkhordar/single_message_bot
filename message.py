class ReadyMessage:
    apology_message = "با عرض پوزش از شما کاربر گرامی،\nبه دلیل ارتقاء بهره وری این سرویس در حال *به روز رسانی* است."


class Regex:
    number_only = '^([0-9]+|[۰-۹]+)$'
    eight_digits_number = "^[0-9]{8}|[۰-۹]{8}$"
    numbers = '([0-9]+|[۰-۹]+)'
    persian_regex = "[ء|\s|آ-ی]+"
    any_match = "(.*)"


class TMessage:
    cancel = "لغو"
    start = "شروع"
    back = "بازگشت به منو اصلی"
    help = "راهنما"


class LogMessage:
    success_send_message = "success send message"
    fail_send_message = "success send message"
    start_conversation = "faced problem"
    max_fail_retried = "max fails retried"
