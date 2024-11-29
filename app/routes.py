from flask import render_template, request, redirect, url_for, flash
from app import app, db, bcrypt
from app.models import User

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Получение данных из формы
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Проверка уникальности пользователя
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or email already exists!', 'danger')
            return redirect(url_for('register'))

        # Хеширование пароля
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Сохранение пользователя в базу данных
        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html')
from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')  # Выводим страницу index.html
