from random import randrange


class Cell:
    def __init__(self, value):
        self.status = "free"
        self.value = value

    def get_status(self):
        return self.status

    def set_status(self):
        self.status = "occupied"

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class TicTacGame:
    def __init__(self):
        self.cells = [Cell("1"), Cell("2"), Cell("3"),
                      Cell("4"), Cell("5"), Cell("6"),
                      Cell("7"), Cell("8"), Cell("9")]

    def show_board(self):
        print("-" * 13)
        print("| " + self.cells[0].value +
              " | " + self.cells[1].value +
              " | " + self.cells[2].value + " |")
        print("-" * 13)
        print("| " + self.cells[3].value +
              " | " + self.cells[4].value +
              " | " + self.cells[5].value + " |")
        print("-" * 13)
        print("| " + self.cells[6].value +
              " | " + self.cells[7].value +
              " | " + self.cells[8].value + " |")
        print("-" * 13)

    def validate_input(self, cell_num):
        if type(cell_num) != str:
            print("Something wrong happening with your input... "
                  "Please try again.")
            return False
        elif len(cell_num) != 1:
            print("Please enter only one (!) symbol "
                  "which is the number of cell you would like to pick 👉👈")
            return False
        elif cell_num not in "123456789":
            print("Please enter the number (!) of cell"
                  " you would like to pick 👉👈")
            return False
        elif self.cells[int(cell_num) - 1].get_status() == "occupied":
            print("Unfortunately, this cell has been "
                  "already selected in this game. "
                  "Please try to pick another one 👉👈")
            return False
        else:
            print("Your choice have been accepted.")
            return True

    def pick_cell(self):
        print("Please, enter number of cell you would like to pick: \n")
        cell_num = input()
        while not self.validate_input(cell_num):
            cell_num = input()
        return int(cell_num)

    def auto_pick_cell(self):
        print("Please, enter number of cell you would like to pick: \n")
        cell_num = str(randrange(1, 10))
        while not self.validate_input(cell_num):
            cell_num = str(randrange(1, 10))
        return int(cell_num)

    def check_winner(self):
        def compare_cells(cell1, cell2, cell3):
            if cell1.get_value() == cell2.get_value() == cell3.get_value():
                return True
            return False

        if (
                compare_cells(self.cells[0], self.cells[1], self.cells[2]) or
                compare_cells(self.cells[0], self.cells[3], self.cells[6]) or
                compare_cells(self.cells[0], self.cells[4], self.cells[8]) or
                compare_cells(self.cells[1], self.cells[4], self.cells[7]) or
                compare_cells(self.cells[2], self.cells[4], self.cells[6]) or
                compare_cells(self.cells[3], self.cells[4], self.cells[5]) or
                compare_cells(self.cells[2], self.cells[5], self.cells[8]) or
                compare_cells(self.cells[6], self.cells[7], self.cells[8])
        ):
            return True
        else:
            print("Still no clear winner...")
            return False

    def p2p_mode(self):
        for i in range(9):
            if i % 2 == 0:
                print("X's turn to pick a cell!")
                cell_num = self.pick_cell() - 1
                self.cells[cell_num].set_status()
                self.cells[cell_num].set_value("X")
            else:
                print("O's turn to pick a cell!")
                cell_num = self.pick_cell() - 1
                self.cells[cell_num].set_status()
                self.cells[cell_num].set_value("O")
            self.show_board()
            if self.check_winner():
                if i % 2 == 0:
                    return "Xs win!"
                else:
                    return "Os win!"
        return "Draw!"

    def p2c_mode(self):
        print('Please choose your role:\n'
              'Enter "x" if you want to play as Xs or '
              'enter any other symbols if you want to play as Os.')
        role = input()
        if role.lower() == "x":
            for i in range(9):
                if i % 2 == 0:
                    print("X's turn to pick a cell!")
                    cell_num = self.pick_cell() - 1
                    self.cells[cell_num].set_status()
                    self.cells[cell_num].set_value("X")
                else:
                    print("O's turn to pick a cell!")
                    cell_num = self.auto_pick_cell() - 1
                    self.cells[cell_num].set_status()
                    self.cells[cell_num].set_value("O")
                self.show_board()
                if self.check_winner():
                    if i % 2 == 0:
                        return "Xs win!"
                    else:
                        return "Os win!"
            return "Draw!"
        else:
            for i in range(9):
                if i % 2 == 0:
                    print("X's turn to pick a cell!")
                    cell_num = self.auto_pick_cell() - 1
                    self.cells[cell_num].set_status()
                    self.cells[cell_num].set_value("X")
                else:
                    print("O's turn to pick a cell!")
                    cell_num = self.pick_cell() - 1
                    self.cells[cell_num].set_status()
                    self.cells[cell_num].set_value("O")
                self.show_board()
                if self.check_winner():
                    if i % 2 == 0:
                        return "Xs win!"
                    else:
                        return "Os win!"
            return "Draw!"

    def c2c_mode(self):
        for i in range(9):
            if i % 2 == 0:
                print("X's turn to pick a cell!")
                cell_num = self.auto_pick_cell() - 1
                self.cells[cell_num].set_status()
                self.cells[cell_num].set_value("X")
            else:
                print("O's turn to pick a cell!")
                cell_num = self.auto_pick_cell() - 1
                self.cells[cell_num].set_status()
                self.cells[cell_num].set_value("O")
            self.show_board()
            if self.check_winner():
                if i % 2 == 0:
                    return "Xs win!"
                else:
                    return "Os win!"
        return "Draw!"

    def start_game(self):
        print('Please, choose a game mod: \n'
              'Enter 1 if you want to play against computer;\n'
              'Enter 2 if you want to play against another player.\n'
              'Enter any other symbols if you want '
              'to watch a game computer against computer;\n')
        mode = int(input())
        self.show_board()
        if mode == 1:
            return self.p2c_mode()
        elif mode == 2:
            return self.p2p_mode()
        else:
            return self.c2c_mode()


if __name__ == '__main__':
    game = TicTacGame()
    print(game.start_game())
