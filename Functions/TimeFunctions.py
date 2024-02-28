from datetime import datetime, timezone
import pytz
import locale

from datetime import datetime


def TimeToMillis(date_time):
    epoch = datetime.fromtimestamp(0)
    delta = date_time - epoch
    return int(delta.total_seconds() * 1000)


def MillisToTime(milliseconds):
    seconds = int(milliseconds) / 1000
    return datetime.fromtimestamp(seconds)


def NanoToTime(nanoseconds):
    seconds = int(nanoseconds) / 1e9
    formatted_date = datetime.fromtimestamp(seconds).strftime("%d/%m/%Y %H:%M:%S")

    return formatted_date


def TimeToNanos(date_time):
    epoch = datetime.fromtimestamp(0)
    delta = date_time - epoch
    return int(delta.total_seconds() * 1e9)


print(NanoToTime(1709068380000000000))