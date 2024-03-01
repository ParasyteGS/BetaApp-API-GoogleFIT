from datetime import datetime, timezone
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
<<<<<<< HEAD
    formatted_date = datetime.fromtimestamp(seconds).strftime("%H:%M:%S")

=======
    formatted_date = datetime.fromtimestamp(seconds).strftime("%d/%m/%Y %H:%M:%S")
>>>>>>> 328c766319312c2d00f79b1737f5973427158936
    return formatted_date


def NanoToTimeWoHours(nanoseconds):
    seconds = int(nanoseconds) / 1e9
    formatted_date = datetime.fromtimestamp(seconds).strftime("%d/%m/%Y")

    return formatted_date


def TimeToNanos(date_time):
    epoch = datetime.fromtimestamp(0)
    delta = date_time - epoch
    return int(delta.total_seconds() * 1e9)
<<<<<<< HEAD
=======


def MillisToMinutes(milliseconds):
    seconds = int(milliseconds) / 1000
    return int(seconds / 60)
>>>>>>> 328c766319312c2d00f79b1737f5973427158936
