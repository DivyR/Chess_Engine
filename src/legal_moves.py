import checkers
import sorts

def GetPieceLegalMoves(board, position):
   piece = board[position]
   if piece == 0:
      return False
   move_functions = [GetPawnMoves, GetKnightMoves, GetBishopMoves, GetRookMoves, GetQueenMoves, GetKingMoves]
   current_row = position//8  # between 0 to 7
   player, opponent = piece//10 * 10, 20
   piece_type = checkers.PieceType(piece)
   if player == 20:
      opponent = 10
   return move_functions[piece_type](board, position, player, opponent, current_row)

def GetPawnMoves(board, position, player, opponent, row):
   moves = []
   restricted = []
   if player == 10:
      factor = 1 
   else:
      factor = -1
   for i in range(position + 7*factor, position + 10*factor, 1*factor):
      if not checkers.InBoard(i) or i//8 != row + factor:
         continue
      elif i == position + 8*factor:
         if board[i] == 0:
            sorts.InsertSort(moves, i)
         else:
            sorts.InsertSort(restricted, i)
         continue
      elif checkers.IsPlayer(board, i, opponent):
         sorts.InsertSort(moves, i)
      else:
         sorts.InsertSort(restricted, i)
   return [moves, restricted]

def GetKnightMoves(board, position, player, opponent, row):
   moves = []
   restricted = []
   for i in range(position - 2*8, position + 3*8, 8):
      if not checkers.InBoard(i) or i == position:
         continue
      elif abs(i//8 - row) == 2:
         l, r = i - 1, i + 1
         if l//8 == i//8:
            if board[l] == 0 or checkers.IsPlayer(board, l, opponent):
               sorts.InsertSort(moves, l)
            else:
               sorts.InsertSort(restricted, l)
         if r//8 == i//8:
            if board[r] == 0 or checkers.IsPlayer(board, r, opponent):
               sorts.InsertSort(moves, r)
            else:
               sorts.InsertSort(restricted, r)
      else:
         l, r = i - 2, i + 2
         if l//8 == i//8:
            if board[l] == 0 or checkers.IsPlayer(board, l, opponent):
               sorts.InsertSort(moves, l)
            else:
               sorts.InsertSort(restricted, l)
         if r//8 == i//8:
            if board[r] == 0 or checkers.IsPlayer(board, r, opponent):
               sorts.InsertSort(moves, r)
            else:
               sorts.InsertSort(restricted, r)
   return [moves, restricted]

def GetBishopMoves(board, position, player, opponent, row):
   moves, directions, n, j = [], [-1, 1, -1, 1], 1, -1
   restricted = []
   while directions != [0, 0, 0, 0]:
      j += 1
      if j > 0 and j % 2 == 0:
         n *= -1
         if j == 4:
            j = 0
            n = abs(n) + 1
      if not directions[j]:
         continue
      index = position + 8*n + directions[j]*n
      if checkers.InBoard(index) and abs(index//8 - row) == abs(n):
         if board[index] == 0:
            sorts.InsertSort(moves, index)
            continue
         elif checkers.IsPlayer(board, index, opponent):
            sorts.InsertSort(moves, index)
         directions[j] = 0
         sorts.InsertSort(restricted, index)
      else:
         directions[j] = 0
         #InsertSort(restricted, index)
   return [moves, restricted] 

def GetRookMoves(board, position, player, opponent, row):
   moves, directions, n, j = [], [[1, 1], [-1, 1], [0, 1], [0, 1]], 1, -1
   restricted = []
   while directions != [[1, 0], [-1, 0], [0, 0], [0, 0]]:
      j += 1
      if j == 4:
         j = 0
         n += 1
      if not directions[j][1]:
         continue
      index = position + 8*n*directions[j][0] + n*directions[abs(3 - j)][0]
      if checkers.InBoard(index) and abs(index//8 - row) == abs(n*directions[j][0]):
         if board[index] == 0:
            sorts.InsertSort(moves, index)
            continue
         elif checkers.IsPlayer(board, index, opponent):
            sorts.InsertSort(moves, index)
         directions[j][1] = 0
         sorts.InsertSort(restricted, index)
      else:
         directions[j][1] = 0
         #InsertSort(restricted, index)
   return [moves, restricted]

def GetQueenMoves(board, position, player, opponent, row):
   moves = []
   restricted = []
   bish_moves = GetBishopMoves(board, position, player, opponent, row)
   rook_moves = GetRookMoves(board, position, player, opponent, row)
   sorts.InsertSort(moves, bish_moves[0])
   sorts.InsertSort(restricted, bish_moves[1])
   sorts.InsertSort(moves, rook_moves[0])
   sorts.InsertSort(restricted, rook_moves[1])
   return [moves, restricted]

def GetKingMoves(board, position, player, opponent, row):
   moves = []
   factor = 1
   restricted = []
   for i in range(position + 7, position + 10, 1):
      if i//8 != row + 1:
         continue
      for j in range(i, i - 8*3, -8):
         if j == position:
            continue
         elif checkers.InBoard(j):
            if checkers.IsPlayer(board, j, player):
               sorts.InsertSort(restricted, j)
            else:
               sorts.InsertSort(moves, j)
   return [moves, restricted]