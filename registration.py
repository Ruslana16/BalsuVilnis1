from flask import Flask, request, render_template_string

@app.route('/register', methods=['POST'])
def register():
    # Логика регистрации пользователя...
    # Если регистрация прошла успешно:
    return render_template_string("""
        <html>
            <head>
                <script>
                    alert("Jūs esat veiksmīgi reģistrējies!");
                    window.location.href = '/ierosinajuma_izveide.html';
                </script>
            </head>
            <body>
                Redirecting...
            </body>
        </html>
        """)

