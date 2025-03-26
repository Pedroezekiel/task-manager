from datetime import datetime


class DateTimeUtils:

    @staticmethod
    def convert_datetime(value):
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        return value