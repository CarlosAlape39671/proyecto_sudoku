class Sudoku:

    def __init__(self):
        self.board = []

    def check_elements(self, info_position):
        info = {"fila": info_position["fila"], "cuadricula": info_position["cuadricula"], "fila_cuadricula": self.get_fila_cuadricula(info_position["posicion"]), "posicion_fila_cuadricula": self.get_position_fila_cuadricula(info_position["posicion"]), "valor": info_position["valor"]}
        right_column = self.check_elements_in_the_columns(info)
        right_row = self.check_elements_in_the_row(info)
        right_grid = self.check_elements_in_the_grid(info)
        return right_column and right_row and right_grid

    def check_elements_in_the_columns(self, info_position):
        right_column = True
        for row in self.board:
            for column_position in range(len(row["columnas"])):
                if column_position == info_position["cuadricula"]:
                    for row_column in row["columnas"][column_position]:
                        if row_column[info_position["posicion_fila_cuadricula"]] == info_position["valor"]:
                            right_column = False
        return right_column

    def check_elements_in_the_row(self, info_position):
        right_row = True
        for row in self.board:
            if row["fila"] == info_position["fila"]:
                for column in row["columnas"]:
                    for element in column[info_position["fila_cuadricula"]]:
                        if element == info_position["valor"] : right_row = False
        return right_row

    def check_elements_in_the_grid(self, info_position):
        right_grid = True
        for row in self.board:
            if row["fila"] == info_position["fila"]:
                for column_position in range(len(row["columnas"])):
                    if column_position == info_position["cuadricula"]:
                        for row_column in row["columnas"][column_position]:
                            for element in row_column:
                                if element == info_position["valor"] : right_grid = False
        return right_grid

    def get_fila_cuadricula(self, position):
        return position // 3

    def get_position_fila_cuadricula(self, position):
        return position % 3

    def set_board(self, board):
        self.board = board