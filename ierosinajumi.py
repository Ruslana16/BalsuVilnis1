from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Ierosinajums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    theme = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Ierosinajums {self.title}>"
from flask import Flask, render_template, request, redirect, url_for
from yourapp import db  # Импортируйте db из вашего основного файла приложения Flask
from yourapp.ierosinajums import Ierosinajums  # Импортируйте модель Ierosinajums

app = Flask(__name__)

@app.route('/create_ierosinajums', methods=['GET', 'POST'])
def create_ierosinajums():
    if request.method == 'POST':
        title = request.form['title']
        theme = request.form['theme']
        description = request.form['description']

        new_ierosinajums = Ierosinajums(title=title, theme=theme, description=description)
        db.session.add(new_ierosinajums)
        db.session.commit()

        return redirect(url_for('visas_aptaujas'))
    return render_template('ierosinajuma_izveide.html')

@app.route('/visas_aptaujas')
def visas_aptaujas():
    ierosinajumi = Ierosinajums.query.all()
    return render_template('aptauju_saraksts.html', ierosinajumi=ierosinajumi)

