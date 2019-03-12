from chessPlayer import *
from time import time
import adams as other
import kanav as other2

def mini_game_other(board):
   player = 10
   printBoard(board)
   while True:
      if player == 20:
         start_time = time()
         while time() - start_time < 2:
            continue
         move = other2.chessPlayer(board, player)[1]
         #print(move)
         print("---", time() - start_time, "seconds ---")
         board[move[1]] = board[move[0]]
         board[move[0]] = 0
         player = 10
         #print("\nADAMS:")
         #print("Best Move:", move, "Score of Position:", score, "Player:", player)
         print("\nBest Move:", move)
         printBoard(board)
      if player == 10:
         start_time = time()
         while time() - start_time < 2:
            continue
         move = chessPlayer(board, player)[1]
         #print(move)
         print("---", time() - start_time, "seconds ---")
         board[move[1]] = board[move[0]]
         board[move[0]] = 0
         player = 20
         #print("Best Move:", move, "Score of Position:", score, "Player:", player)
         print("\nBest Move:", move)
         printBoard(board)
   return True

mini_game_other(GenBoard())