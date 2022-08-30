from datetime import datetime

def convert_to_datetime(js_date):
    return datetime.fromtimestamp(js_date / 1000.0)