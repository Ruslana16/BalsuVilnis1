# manage_users.py
import sqlite3

def add_user(username, email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', 
              (username, email, password))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Тестирование функции добавления пользователя
    add_user('testuser', 'user@example.com', 'securepassword123')
