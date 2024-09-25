from flask import request, redirect, url_for, render_template, flash, session
from app.models import User, Student, PcsModel, Role
from app import db

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from passlib.hash import pbkdf2_sha256

class UserForm(FlaskForm):
    name = StringField('Name', 
                        validators=[DataRequired()], 
                        render_kw={"class": "form-control", "placeholder": "Enter your name"})
    username = StringField('Username', 
                           validators=[DataRequired(message="Username tidak boleh kosong."), Length(min=3, max=50,message="Username harus antara 3 sampai 50 karakter.")], 
                           render_kw={"class": "form-control", "placeholder": "Enter your username"})
    email = StringField('Email', 
                        validators=[DataRequired(), Email()], 
                        render_kw={"class": "form-control", "placeholder": "Enter your email"})
    password = PasswordField('Password',
                        render_kw={"class": "form-control", "placeholder": "Enter your password"})
    
    role_id = SelectField('Pilih Role', choices=[], coerce=int, validate_choice=False, validators=[DataRequired()])
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})

    # validators=[DataRequired(), Length(min=3, max=50,message="Password harus antara 3 sampai 50 karakter.")]

    def __init__(self, original_username=None, original_email=None, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

        # Ambil argumen 'is_edit' dari kwargs, default False (create mode)
        self.is_edit = kwargs.pop('is_edit', False)

        # Hanya wajibkan email ketika bukan mode edit
        if not self.is_edit:
            # jika False
            # validation ada setelah di submit, required dan min max length
            self.password.validators = [DataRequired(), Length(min=3, max=50,message="Password harus antara 3 sampai 50 karakter.")]
            # self.password.validators.append(DataRequired(), Length(min=3, max=50,message="Password harus antara 3 sampai 50 karakter."))
        


    # Custom validator untuk memastikan username unik
    def validate_username(self, username):
        # Jika mode edit dan username tidak berubah, tidak perlu validasi unik
        if self.original_username and self.original_username == username.data:
            return
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username sudah digunakan. Silakan pilih username lain.')

    # Custom validator untuk memastikan email unik
    def validate_email(self, email):
        # Jika mode edit dan email tidak berubah, tidak perlu validasi unik
        if self.original_email and self.original_email == email.data:
            return
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email sudah digunakan. Silakan pilih email lain.')
        
    def validate_role_id(self, field):
        role = Role.query.get(field.data)
        if not role:
            raise ValidationError('Role tidak valid. Silakan pilih role yang benar.')
        
class ChangePasswordFrom(FlaskForm):
    old_password = PasswordField('Old Password',
                             validators=[ Length(min=3,message="Password min 3")],
                        render_kw={"class": "form-control", "placeholder": "Enter your password"})
    password = PasswordField('New Password',
                             validators=[ Length(min=3,message="Password min 3")],
                        render_kw={"class": "form-control", "placeholder": "Enter your password"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo(fieldname="password", message="Password harus sama"), Length(min=3,message="Password min 3")],
                        render_kw={"class": "form-control", "placeholder": "Confirm your password"})
    
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})

    def validate_old_password(self, field):
        old_password = field.data
        username = session['username']
        data = User.query.filter(
            (User.username ==username) | (User.email== username)
        ).first()
        if data:
            hash = data.password
            if ((pbkdf2_sha256.verify(old_password, hash)) == False) :
                raise ValidationError('Password wrong')
        else: 
            raise ValidationError('User not found')

def index():
    form = FlaskForm()
    data = User.query.all()
    print(Student.query.all())
    print(Student.get_student())
    # print(PcsModel.getProductionData('V01'))
    students = Student.get_student()

    data = {
        'title' : 'View Users',
        'data' : data
    }
    return render_template('users/index.html', data=data, students = students, form=form)

def new():
    form = UserForm()
    data = {
        'title' : 'New user',
        'roles' : Role.query.all()
    }

    form.role_id.choices = [(role.id, role.title) for role in data['roles']]
    return render_template('users/new.html', data=data, form=form)

def create():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            role_id = request.form['role_id']
            password = request.form['password']
            password = pbkdf2_sha256.hash(password)
            user = User(name=name,username=username, email=email, password=password, role_id=role_id)
            db.session.add(user)
            db.session.commit()
            flash('User created successfully!', 'message')
            return redirect(url_for('users.index'))
        else:
            return render_template('users/new.html', form=form)
    
def edit(id):
    result = User.query.get_or_404(id)
    form = UserForm(original_username=result.username, original_email=result.email, is_edit=True)
    data = {
        'title' : 'Edit user',
        'data' : result,
        'roles' : Role.query.all()
    }
    form.role_id.choices = [(role.id, role.title) for role in data['roles']]
    form.role_id.data = result.role_id  # Pre-select pilihan dropdown
    return render_template('users/edit.html', data=data, form=form)

def update(id):
    user = User.query.get_or_404(id)
    form = UserForm(original_username=user.username, original_email=user.email, is_edit=True)
    # print(request.method)
    if form.validate_on_submit():
        user.name = request.form['name']
        user.username = request.form['username']
        user.email = request.form['email']
        user.role_id = request.form['role_id']
        password = request.form['password']
        user.password = pbkdf2_sha256.hash(password)
        db.session.commit()
        flash('User updated successfully!', 'message')
        return redirect(url_for('users.index'))
    else:
        data = User.query.get_or_404(id)
        return render_template('users/edit.html', data=data, form=form)
        
    
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'message')
    return redirect(url_for('users.index'))

def change_password():
    form = ChangePasswordFrom()
    data = {
        'title' : 'Change Password',
    }

    return render_template('users/change_password.html', data=data, form=form)

def update_password():
    form = ChangePasswordFrom()
    if form.validate_on_submit():
        return 'okok'
    else :
        data = {
            'title' : 'Change Password',
        }

        return render_template('users/change_password.html', data=data, form=form)