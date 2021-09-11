from flask import Flask
from flask import render_template, request

from forms import UniverseSize
from game_of_life import GameOfLife


app = Flask(__name__)
app.secret_key = 'you_need_a_secret_key'


width, height = 20, 15


@app.route('/', methods=['get', 'post'])
def index():
    global width, height
    form = UniverseSize()
    if request.method == 'POST' and form.validate_on_submit():
        w_str = request.form.get('width')
        width = int(w_str) if w_str else width
        h_str = request.form.get('height')
        height = int(h_str) if h_str else height
    GameOfLife(width=width, height=height)
    return render_template('index.html', width=width, height=height, size=form)


@app.route('/live')
def live():
    game = GameOfLife()
    game.form_new_generation()
    return render_template('live.html',
                           life=game)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
