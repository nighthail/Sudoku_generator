from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    board_zeroes = np.zeros(shape=(9, 9), dtype=int)
    board_init = board_zeroes.copy()
    board_init[0, :] = [0, 0, 0, 0, 0, 0, 5, 7, 3]
    board_init[1, :] = [0, 0, 0, 0, 0, 0, 5, 7, 3]
    board_init[2, :] = [0, 0, 0, 0, 0, 0, 5, 7, 3]
    board_init[3, :] = [0, 1, 0, 0, 0, 0, 5, 7, 3]
    board_init[4, :] = [0, 0, 0, 0, 0, 0, 5, 7, 3]
    board_init[5, :] = [1, 0, 0, 0, 0, 0, 5, 7, 3]
    board_init[6, :] = [0, 0, 0, 0, 0, 0, 5, 7, 3]
    board_init[7, :] = [0, 0, 0, 0, 0, 0, 5, 7, 3]
    board_init[8, :] = [0, 0, 0, 0, 0, 0, 5, 7, 3]

    # Pass the board_init array to the templatex

    return render_template('index.html', board_init=board_init)

if __name__ == '__main__':
    app.run(debug=True)
