import datetime
from flask import render_template, redirect, url_for, request, abort, session, flash, get_flashed_messages

def format_date(date):
    """Helper function untuk memformat tanggal ke format DD-MM-YYYY."""
    return date.strftime('%d-%m-%Y') if isinstance(date, datetime.date) else None

def greet_user(name = 'saepul'):
    """Helper function untuk menyapa user."""
    return f'Hello, {name}!'

def hello_user(name = 'saepul'):
    """Helper function untuk menyapa user."""
    return f'Hello, {name}!'


def setAlert(icon = 'success', title = 'Success', text = 'Test', type = 'sweetalert') :
    # session['icon'] = icon
    # session['title'] = title
    # session['text'] = text
    flash(icon, 'icon')
    flash(title, 'title')
    flash(text, 'text')
    flash(type, 'type')
    # flash(url, 'url')

def initAlert():
    icon = session['icon'] if 'icon' in session else ''
    title = session['title'] if 'title' in session else ''
    text = session['text'] if 'text' in session else ''

    icon = get_flashed_messages(category_filter=["icon"])
    title = get_flashed_messages(category_filter=["title"])
    text = get_flashed_messages(category_filter=["text"])
    type = get_flashed_messages(category_filter=["type"])
    url = get_flashed_messages(category_filter=["url"])

    icon = icon[0] if icon else ''
    title = title[0] if title else ''
    text = text[0] if text else ''
    type = type[0] if type else ''
    url = url[0] if url else ''

    load = '<div id="flash" data-icon="' + icon + '" data-title="' + title + '" data-text="' + text + '" data-type="' + type + '"  ></div> '

    load = load + """ <script>

                    const Swal2 = Swal.mixin({
                        customClass: {
                        input: 'form-control'
                        }
                    })
                    
                    const Toast = Swal.mixin({
                        toast: true,
                        position: 'top-end',
                        showConfirmButton: false,
                        timer: 3000,
                        timerProgressBar: true,
                        didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                        }
                    })
                    
                    
                    function deleteTombol(e){
                        const ket = e.getAttribute('data-ket');
                        const href = e.getAttribute('data-href') ? e.getAttribute('data-href') : e.getAttribute('href');
                        Swal.fire({
                        title: 'Are you sure?',
                        text: ket,
                        icon: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#3085d6',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Yes, delete it!'
                        }).then((result) => {
                        if (result.value) {
                            if(href){
                            window.location.href = href;
                            }else{
                            e.parentElement.submit();
                            }
                        }
                        })
                        e.preventDefault();
                    }
                    
                    const iconFlash = document.getElementById('flash').getAttribute('data-icon');
                    const titleFlash = document.getElementById('flash').getAttribute('data-title');
                    const textFlash = document.getElementById('flash').getAttribute('data-text');
                    const urlFlash = document.getElementById('flash').getAttribute('data-url');
                    const typeFlash = document.getElementById('flash').getAttribute('data-type');


                    if(typeFlash == 'sweetalert'){
                        
                        if (iconFlash && urlFlash) {
                        Swal.fire({
                            icon: iconFlash,
                            title: titleFlash,
                            text: textFlash
                        }).then((result) => {
                            if (result.value) {
                            window.location.href = urlFlash;
                            }
                        })
                        } else if (iconFlash) {
                        Swal.fire({
                            icon: iconFlash,
                            title: titleFlash,
                            text: textFlash
                        })
                        }

                    }else if(typeFlash =='toast'){
                        Toast.fire({
                        icon: iconFlash,
                        title: titleFlash
                        })
                    }

                    </script> """
    # print(load)
    return load