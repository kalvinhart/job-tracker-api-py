from datetime import datetime

def convert_to_datetime(js_date):
    if js_date is not None:
        return datetime.fromtimestamp(js_date / 1000.0)

    return None