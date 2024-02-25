# app.py
from flask import Flask, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def add_user(username, email, password):
    # Та же функция добавления пользователя
    ...

@app.route('/register', methods=['POST'])
def register():
    # Логика обработки регистрационной формы
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']  # В реальном приложении пароль должен быть захеширован
    add_user(username, email, password)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

