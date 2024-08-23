from flask import request, redirect, url_for, render_template, flash

def index() :
    return render_template('welcome_message.html') 
