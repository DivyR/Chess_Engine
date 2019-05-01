import sorts
import legal_moves

def IsPositionUnderThreat(opponent_board, position):
   for i in range(0, len(opponent_board), 1):
      if sorts.BinarySearch(opponent_board[i][2], position) != -1:
         return True
   return False

def IsPositionRestricted(player_board, position):
   for i in range(0, len(player_board), 1):
      a = sorts.BinarySearch(player_board[i][3], position)
      if a != -1:
         return i
   return -1

def InBoard(index):
   if index < 0 or index > 63:
      return False
   return True

def IsPlayer(board, index, player):
   if board[index] < player or board[index] > player + 5:
      return False
   return True

def GenOpponent(player):
   if player == 10:
      return 20
   elif player == 20:
      return 10
   return False

def PieceType(piece):
   if piece == 0:
      return -1
   return int(str(piece)[1])

def GetPlayerPositions(board, player):
   positions = []
   for i in range(0, 64, 1):
      if IsPlayer(board, i, player):
         sorts.InsertSort(positions, i)
   return positions

def GenPlayerData(board):  # [piece, position, [availible moves]]
   player_data = [[], []]
   for i in range(0, 2, 1):
      player_data[i] = GetPlayerPositions(board, (i+1)*10)
      for j in range(0, len(player_data[i]), 1):
         pos = player_data[i][j]
         moves_restricted = legal_moves.GetPieceLegalMoves(board, pos)
         player_data[i][j] = [board[pos]] + [pos] + [moves_restricted[0]] + [moves_restricted[1]]
   return player_data