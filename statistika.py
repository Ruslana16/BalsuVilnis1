from flask import Flask, render_template
import plotly.graph_objs as go

app = Flask(__name__)

# Данные о голосах (пример данных)
votes_for = 75
votes_against = 25

@app.route('/')
def index():
    # Рассчитываем проценты голосов
    total_votes = votes_for + votes_against
    percent_for = (votes_for / total_votes) * 100
    percent_against = (votes_against / total_votes) * 100

    # Создаем график
    fig = go.Figure()
    fig.add_trace(go.Bar(x=['ЗА', 'ПРОТИВ'], y=[percent_for, percent_against]))

    # Конфигурируем макет графика
    fig.update_layout(title='Голоса ЗА и ПРОТИВ',
                      xaxis_title='Голоса',
                      yaxis_title='Проценты')

    # Конвертируем график в HTML
    graph_html = fig.to_html(full_html=False)

    # Отображаем HTML страницу с графиком
    return render_template('statistika.html', graph=graph_html)

if __name__ == '__main__':
    app.run(debug=True)