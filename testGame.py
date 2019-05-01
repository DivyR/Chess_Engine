import sys
sys.path.insert(0, "lib")
from time import time
import chessPlayer as cpu
import boards

def test_game(board, player):
   boards.printBoard(board)
   while True:
      if player == 10:
         start_time = time()
         while time() - start_time < 2:
            continue
         move = cpu.chessPlayer(board, player)[1]
         print("---", time() - start_time, "seconds ---")
         board[move[1]] = board[move[0]]
         board[move[0]] = 0
         player = 20
         print("\nBest Move:", move)
         boards.printBoard(board)
      if player == 20:
         start_time = time()
         while time() - start_time < 2:
            continue
         move = cpu.chessPlayer(board, player)[1]
         print("---", time() - start_time, "seconds ---")
         board[move[1]] = board[move[0]]
         board[move[0]] = 0
         player = 10
         print("\nBest Move:", move)
         boards.printBoard(board)
   return True

test_game(boards.GenBoard(), 10)