import datetime

def format_date(date):
    """Helper function untuk memformat tanggal ke format DD-MM-YYYY."""
    return date.strftime('%d-%m-%Y') if isinstance(date, datetime.date) else None

def greet_user(name):
    """Helper function untuk menyapa user."""
    return f'Hello, {name}!'
