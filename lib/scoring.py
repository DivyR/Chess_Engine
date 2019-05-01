import checkers
import sorts

def PieceValue(piece):  # generate a score depending on the peice
   pt = checkers.PieceType(piece)
   factor = -1
   if piece//10 == 1:
      factor = 1
   if pt == 0:
      return 100 * factor
   elif pt == 1:
      return 150 * factor
   elif pt == 2:
      return 150 * factor
   elif pt == 3:
      return 200 * factor
   elif pt == 4:
      return 250 * factor
   elif pt == 5:
      return 10000 * factor
   return 0

def SafetyRating(player, pd, depth):  # generate a score depending on the safety of the peices ...
   p_i = player//10 - 1        # 0 is best, negative_relative score for any threatened pieces
   o_i = checkers.GenOpponent(player)//10 - 1
   score = 0
   factor = -1
   b = -1
   for i in range(0, len(pd[p_i]), 1):
      for j in range(0, len(pd[o_i]), 1):
         b = sorts.BinarySearch(pd[o_i][j][2], pd[p_i][i][1])
         if b != -1:
            break
      if b == -1:
         continue
      pv = PieceValue(pd[p_i][i][0])
      a = checkers.IsPositionRestricted(pd[p_i], pd[p_i][i][1]) 
      if a == -1 or abs(pv) == 10000:
         score += pv/2 * factor * 1 #(depth + 1)
      #elif a != -1:
         #if PieceType(pd[p_i][a][0]) > PieceType(pd[o_i][j][0]):
         #   score += pv/2 * factor * (depth + 1)
         #else:
         #score += 3
   return score

def PositionValue(piece_id, position):  # gens score depending on piece location from centre
   player = (piece_id//10) * 10
   if player == 10:
      factor = 1
   else:
      factor = -1
   piece_type = checkers.PieceType(piece_id)
   pr_functions = [PawnPV, KnightPV, BishopPV, RookPV, QueenPV, KingPV]
   return pr_functions[piece_type](factor, position)

def PositionRadius(position):  # helper to find piece distance from center
   if position in [27, 28, 35, 26]:
      return 0
   c1 = 0
   while (position - c1) % 8 != 0:
      c1 += 1
   if c1 == 0 or c1 == 7 or position - c1 == 56 or position - c1 == 0:
      return 3
   row = position//8
   if row == 1 or row == 6 or (position + 2) % 8 == 0 or (position - 1) % 8 == 0:
      return 2
   else:
      return 1

def PawnPV(factor, position):  # Pawn'PositionValue'
   value = PositionRadius(position)
   if value == 0:
      return 22 * factor
   elif value == 1:
      return 17 * factor
   elif value == 2:
      return 10 * factor
   else:
      return 0 * factor

def KnightPV(factor, position):
   value = PositionRadius(position)
   if value == 0:
      return 0 * factor
   elif value == 1:
      return 15 * factor
   elif value == 2:
      return 10 * factor
   else:
      return -50 * factor

def BishopPV(factor, position):
   value = PositionRadius(position)
   if value == 0:
      return 5 * factor
   elif value == 1:
      return 10 * factor
   elif value == 2:
      return 25 * factor
   else:
      return 5 * factor

def RookPV(factor, position):
   value = PositionRadius(position)
   if value == 0 or value == 1:
      return 5 * factor
   elif value == 2:
      return 15 * factor
   else:
      return 10 * factor

def QueenPV(factor, position):
   value = PositionRadius(position)
   if value == 0:
      return 10 * factor
   elif value == 1:
      return 10 * factor
   elif value == 2:
      return 10 * factor
   else:
      return 5 * factor

def KingPV(factor, position):
   value = PositionRadius(position)
   if value == 0:
      return 5 * factor
   elif value == 1:
      return 10 * factor
   elif value == 2:
      return 10 * factor
   else:
      return 15 * factor

def OptionsRating(piece_id, moves):  # generates a score depending on the number of moves a piece can make
   player = (piece_id//10) * 10
   or_functions = [PawnOR, KnightOR, BishopOR, RookOR, QueenOR, KingOR]
   if player == 10:
      factor = 1
   else:
      factor = -1
   piece_type = checkers.PieceType(piece_id)
   return or_functions[piece_type](moves, factor)

def PawnOR(moves, factor):
   return len(moves) * 7 * factor

def KnightOR(moves, factor):
   return len(moves) * 2 * factor

def BishopOR(moves, factor):
   return len(moves) * 3 * factor

def RookOR(moves, factor):
   return len(moves) * 2 * factor

def QueenOR(moves, factor):
   return len(moves) * 2 * factor

def KingOR(moves, factor):
   return (8 - len(moves)) * 3 * factor

def RankHeavy(player, pd):  # score depending on how heavy back rank is, less points for more on back rank
   p_i = player//10 - 1
   counter = 0
   row = 7
   factor = 1
   if player == 10:
      row = 0
      factor = -1
   for i in range(0, len(pd[p_i]), 1):
      if pd[p_i][i][1]//8 != row or checkers.PieceType(pd[p_i][i][0]) == 5:
         continue
      counter += 1
   return pow(counter, 2.2) * factor

def RooksConnected(player_data):  # returns a score depending on if the rooks are connected or not
   score = 0
   for i in range(0, 2, 1):
      player = (i + 1) * 10
      rook_id, indices = player + 3, []
      for j in range(0, len(player_data[i]), 1):
         if player_data[i][j][0] == rook_id:
            indices += [j]
            if len(indices) == 2:
               if sorts.BinarySearch(player_data[i][indices[0]][3], player_data[i][indices[1]][1]) != -1:
                  factor = 1
                  if player == 10:
                     factor = -1
                  score += 5 * factor
                  break
   return score