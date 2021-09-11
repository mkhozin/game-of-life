from flask import Flask
from flask import render_template, request

from game_of_life import GameOfLife


app = Flask(__name__)


width, height = 20, 15


@app.route('/', methods=['get', 'post'])
def index():
    global width, height
    if request.method == 'POST':
        w_str = request.form.get('width')
        width = int(w_str) if w_str else width
        h_str = request.form.get('height')
        height = int(h_str) if h_str else height
    GameOfLife(width=width, height=height)
    return render_template('index.html', width=width, height=height)


@app.route('/live')
def live():
    game = GameOfLife()
    game.form_new_generation()
    return render_template('live.html',
                           life=game)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
