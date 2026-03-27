from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    title = request.args.get('title', 'Подготовка к миссии')
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    prof_lower = prof.lower()
    is_engineering = 'инженер' in prof_lower or 'строитель' in prof_lower

    if is_engineering:
        training_title = "Инженерные тренажеры"
    else:
        training_title = "Научные симуляторы"

    return render_template('training.html', title=training_title, training_title=training_title,
                           profession=prof, is_engineering=is_engineering)


if __name__ == '__main__':
    app.run()
