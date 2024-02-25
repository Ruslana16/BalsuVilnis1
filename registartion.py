from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Эмуляция базы данных для хранения зарегистрированных пользователей
registered_users = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Получаем данные из формы
        nickname = request.form['nickname']
        email = request.form['email']
        password = request.form['password']

        # Проверяем, существует ли пользователь с таким email
        if email in registered_users:
            return "Пользователь с таким email уже зарегистрирован!"

        # Сохраняем данные пользователя (обычно здесь происходило бы добавление в базу данных)
        registered_users[email] = {'nickname': nickname, 'password': password}

        # Перенаправляем пользователя на страницу профиля
        return redirect(url_for('profile'))

    # Если метод запроса GET, просто отображаем страницу регистрации
    return render_template('registration.html')


@app.route('/profile')
def profile():
    # Здесь обычно происходит логика для отображения профиля пользователя
    # Например, можно получить данные о пользователях из базы данных и передать их в шаблон
    return render_template('profils.html')


if __name__ == '__main__':
    app.run(debug=True, port=5500)