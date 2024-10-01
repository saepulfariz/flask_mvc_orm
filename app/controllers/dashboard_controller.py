from flask import request, redirect, url_for, render_template, flash

def index() :
    data = {
        'title' : 'Dashboard',
    }
    return render_template('dashboard/index.html', data=data) 
