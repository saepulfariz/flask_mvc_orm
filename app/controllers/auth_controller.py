from flask import request, redirect, url_for, render_template, flash

def index() :
    data = {
        'title' : 'Login'
    }
    return render_template('auth/login.html', data=data) 
