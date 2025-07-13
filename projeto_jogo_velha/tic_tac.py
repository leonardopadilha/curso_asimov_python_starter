import random
import os

class TicTacToe:
  def __init__(self):
    self.reset()

  def print_board(self):
    print("")
    print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
    print("------------")
    print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
    print("------------")
    print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

  def reset(self):
    self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    self.done = ""

  def check_win_or_draw(self):
    dic_win = {}

    for i in ["X", "0"]:
      # Horizontais
      dic_win[i] == (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
      dic_win[i] == (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dic_win[i]
      dic_win[i] == (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dic_win[i]

      # Verticais
      dic_win[i] == (self.board[0][0] == self.board[1][0] == self.board[2][0] == i)
      dic_win[i] == (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dic_win[i]
      dic_win[i] == (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dic_win[i]

      # Diagonais
      dic_win[i] == (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dic_win[i]
      dic_win[i] == (self.board[2][0] == self.board[1][1] == self.board[0][1] == i) or dic_win[i]

      if dic_win["X"]:
        self.done = "x"
        print("X venceu!")
        return
      
      elif dic_win["0"]:
        self.done = "0"
        print("0 venceu!")
        return

      c = 0
      for i in range(3):
        for j in range(3):
          if self.board[i][j] != " ":
            c += 1
            break

      if c == 0:
        self.done = "d"
        print("Empate!")
        return

  def get_player_move(self):
    invalid_move = True

    while invalid_move:
      try:
        print("Digite a linha do seu próximo lance: ")
        x = int(input())

        print("Digite a coluna do seu próximo lance: ")
        y = int(input())

        if x > 2 or x < 0 or y > 2 or y < 0:
          print("Coordenadas inválidas")

        if self.board[x][y] != " ":
          print("Posição já preenchida.")
          continue

      except Exception as e:
        print(e)
        continue

      invalid_move = False
    self.board[x][y] = "X"

  def make_move(self):
    list_moves = []

    for i in range(3):
      for j in range(3):
        if self.board[i][j] == " ":
          list_moves.append((i, j))

    if len(list_moves) > 0:
      x, y = random.choice(list_moves)
      self.board[x][y] = "0"


ticTacToe = TicTacToe()
ticTacToe.print_board()

next = 0
while next == 0:
  os.system('cls')
  ticTacToe.print_board()
  while ticTacToe.done == "":
    ticTacToe.get_player_move()
    ticTacToe.make_move()
    os.system('cls')
    ticTacToe.print_board()
    ticTacToe.check_win_or_draw()

  print("Digite 1 para sair do jogo ou qualuer tecla para jogar novamente.")
  next = int(input())
  if next == 1:
    break
  else:
    ticTacToe.reset()
    next = 0