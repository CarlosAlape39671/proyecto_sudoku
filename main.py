from flask import Flask, request, jsonify
from sudoku.sudoku import Sudoku


print("Hello world")

board = [
    {
        "fila": 1,
        "columnas": [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ]
    },
    {
        "fila": 2,
        "columnas": [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ]
    },
    {
        "fila": 3,
        "columnas": [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ]
    }
]

app = Flask(__name__)
new_game = Sudoku()
new_game.set_board(board)

@app.route('/play', methods=['POST'])
def insert_value():
    info_position = request.get_json()
    if new_game.check_elements(info_position):
        respuesta = {
            "mensaje": "the element was correctly inserted"
        }
    else:
        respuesta = {
            "mensaje": "The element is not allowed"
        }
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)