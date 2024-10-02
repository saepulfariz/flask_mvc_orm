import datetime
from flask import render_template, redirect, url_for, request, abort, session, flash

def format_date(date):
    """Helper function untuk memformat tanggal ke format DD-MM-YYYY."""
    return date.strftime('%d-%m-%Y') if isinstance(date, datetime.date) else None

def greet_user(name = 'saepul'):
    """Helper function untuk menyapa user."""
    return f'Hello, {name}!'


def setAlert(icon = 'success', title = 'Success', text = 'Test') :
    # session['iconFlash'] = icon
    # session['titleFlash'] = title
    # session['textFlash'] = text
    flash(icon, 'icon')
    flash(title, 'title')
    flash(text, 'text')

def initAlert():
    icon = session['iconFlash'] if 'iconFlash' in session else ''
    title = session['titleFlash'] if 'titleFlash' in session else ''
    text = session['textFlash'] if 'textFlash' in session else ''
    load = '<div id="flash" data-icon="' + icon + '" data-title="' + title + '" data-text="' + text + '" data-url=""></div>'
    print(load)
    return load