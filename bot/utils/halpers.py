import datetime


def get_current_time():
    """
    Возвращает текущее время в формате HH:MM.
    """
    now = datetime.datetime.now()
    return f"{now.hour:02d}:{now.minute:02d}"
