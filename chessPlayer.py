from time import time 
#full = time()


#########################
## EXTRAS (not needed) ##
#########################

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   print(accum)
   return True

def indexBoard():
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(i)
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   print(accum)
   return True

def GenBoard():
   board = []
   for i in range(0, 64, 1):
      if i >= 16 and i <= 47:  # no pieces
         board += [0]
      elif i <= 7:  # back w rank
         if i == 0 or i == 7:  # w rooks
            board += [13]
         elif i == 1 or i == 6:  # w knights
            board += [11]
         elif i == 2 or i == 5:  # w bishops
            board += [12]
         elif i == 3:  # w king
            board += [15]
         else:  # w queen
            board += [14]
      elif i <= 15:  # w pawns
         board += [10]
      elif i >= 48 and i <=55:  # b pawns 
         board += [20]
      elif i >=56:  # back b rank
         if i == 56 or i == 63:  # b rooks
            board += [23]
         elif i == 57 or i == 62:  # b knights
            board += [21]
         elif i == 58 or i == 61:  # b bishops
            board += [22]
         elif i == 59:  # b king
            board += [25]
         else:  # b queen
            board += [24]
   return board

#################
## ADT Classes ##
#################

class Queue:

   def __init__(self):
      self.store = []
   
   def put(self, data):
      self.store += [data]
      return True
   
   def get(self):
      data = self.store[0]
      self.store = self.store[1:]
      return data

class Stack:

   def __init__(self):
      self.store = []
   
   def push(self, data):
      self.store += [data]
      return True
   
   def pop(self):
      data = self.store[-1]
      self.store = self.store[:-1]
      return data
   
   def is_empty(self):
      return len(self.store) == 0

#############################
## SORT FUNCTIONS/SEARCHES ##
#############################

def InsertSort(array, data):  # sort moves to allow for BinarySearching
   if type(data) != list:
      array += [data]
   elif data != []:
      array += [data[0]]
      InsertSort(array, data[1::])
   for i in range(len(array) - 1, 0, -1):
      swap_flag = False
      for j in range(i, len(array) - i - 1, -1):
         if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            swap_flag = True
      if not swap_flag:
         break
   return True

def InsertSortNodes(array, nodes):  # sorting evalTree nodes by score
   if type(nodes) != list:
      array += [nodes]
   elif nodes != []:
      array += [nodes[0]]
      InsertSortNodes(array, nodes[1::])
   for i in range(len(array) - 1, 0, -1):
      swap_flag = False
      for j in range(i, len(array) - i - 1, -1):
         if array[j].score < array[j - 1].score:
            array[j], array[j - 1]= array[j - 1], array[j]
            swap_flag = True
      if not swap_flag:
         break
   return True

def BubbleSortNodes(array):  # sorting evalTree nodes by score
   for i in range(0, len(array), 1):
      swap_flag = False
      for j in range(0, len(array) - 1 - i, 1):
         if array[j].bcm[1] > array[j + 1].bcm[1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            swap_flag = True
      if not swap_flag:
         break
   return True

def BubbleSort(array):  # created incase
   for i in range(0, len(array), 1):
      swap_flag = False
      for j in range(0, len(array) - 1 - i, 1):
         if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            swap_flag = True
      if not swap_flag:
         break
   return True

def BubbleSortPDPos(array):  # Sort pd list depending on position
   for i in range(0, len(array), 1):
      swap_flag = False
      for j in range(0, len(array) - 1 - i, 1):
         if array[j][1] > array[j + 1][1]:
            swap = list(array[j])
            swap[2] = list(array[j][2])
            array[j] = list(array[j + 1])
            array[j][2] = list(array[j + 1][2])
            array[j + 1] = list(swap)
            swap_flag = True
      if not swap_flag:
         break
   return True

def BinarySearch(array, data):  # Search for specific moves of pieces
   start, end = 0, len(array) - 1
   while start <= end:
      middle = (end + start)//2
      mid_val = array[middle]
      if mid_val == data:
         return middle
      elif mid_val < data:
         start = middle + 1
      else:
         end = middle - 1
   return -1

def BinarySearchPDPos(array, data):  # search by piece locations
   start, end = 0, len(array) - 1
   while start <= end:
      middle = (end + start)//2
      mid_val = array[middle][1]
      if mid_val == data:
         return middle
      elif mid_val < data:
         start = middle + 1
      else:
         end = middle - 1
   return -1

#####################################
## HELPER FUNCTIONS //Additionals  ##
#####################################

def IsPositionUnderThreat(opponent_board, position):
   for i in range(0, len(opponent_board), 1):
      if BinarySearch(opponent_board[i][2], position) != -1:
         return True
   return False

def IsPositionRestricted(player_board, position):
   for i in range(0, len(player_board), 1):
      a = BinarySearch(player_board[i][3], position)
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
         InsertSort(positions, i)
   return positions

def GenPlayerData(board):  # [piece, position, [availible moves]]
   player_data = [[], []]
   for i in range(0, 2, 1):
      player_data[i] = GetPlayerPositions(board, (i+1)*10)
      for j in range(0, len(player_data[i]), 1):
         pos = player_data[i][j]
         moves_restricted = GetPieceLegalMoves(board, pos)
         player_data[i][j] = [board[pos]] + [pos] + [moves_restricted[0]] + [moves_restricted[1]]
   return player_data

################################
## SCORE GENERATING FUNCTIONS ##
################################

def PieceValue(piece):  # generate a score depending on the peice
   pt = PieceType(piece)
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
   o_i = GenOpponent(player)//10 - 1
   score = 0
   factor = -1
   b = -1
   for i in range(0, len(pd[p_i]), 1):
      for j in range(0, len(pd[o_i]), 1):
         b = BinarySearch(pd[o_i][j][2], pd[p_i][i][1])
         if b != -1:
            break
      if b == -1:
         continue
      pv = PieceValue(pd[p_i][i][0])
      a = IsPositionRestricted(pd[p_i], pd[p_i][i][1]) 
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
   piece_type = PieceType(piece_id)
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
   piece_type = PieceType(piece_id)
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
      if pd[p_i][i][1]//8 != row or PieceType(pd[p_i][i][0]) == 5:
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
               if BinarySearch(player_data[i][indices[0]][3], player_data[i][indices[1]][1]) != -1:
                  factor = 1
                  if player == 10:
                     factor = -1
                  score += 5 * factor
                  break
   return score

###########################
## GET PIECE LEGAL MOVES ##
###########################

def GetPieceLegalMoves(board, position):
   piece = board[position]
   if piece == 0:
      return False
   move_functions = [GetPawnMoves, GetKnightMoves, GetBishopMoves, GetRookMoves, GetQueenMoves, GetKingMoves]
   current_row = position//8  # between 0 to 7
   player, opponent = piece//10 * 10, 20
   piece_type = PieceType(piece)
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
      if not InBoard(i) or i//8 != row + factor:
         continue
      elif i == position + 8*factor:
         if board[i] == 0:
            InsertSort(moves, i)
         else:
            InsertSort(restricted, i)
         continue
      elif IsPlayer(board, i, opponent):
         InsertSort(moves, i)
      else:
         InsertSort(restricted, i)
   return [moves, restricted]

def GetKnightMoves(board, position, player, opponent, row):
   moves = []
   restricted = []
   for i in range(position - 2*8, position + 3*8, 8):
      if not InBoard(i) or i == position:
         continue
      elif abs(i//8 - row) == 2:
         l, r = i - 1, i + 1
         if l//8 == i//8:
            if board[l] == 0 or IsPlayer(board, l, opponent):
               InsertSort(moves, l)
            else:
               InsertSort(restricted, l)
         if r//8 == i//8:
            if board[r] == 0 or IsPlayer(board, r, opponent):
               InsertSort(moves, r)
            else:
               InsertSort(restricted, r)
      else:
         l, r = i - 2, i + 2
         if l//8 == i//8:
            if board[l] == 0 or IsPlayer(board, l, opponent):
               InsertSort(moves, l)
            else:
               InsertSort(restricted, l)
         if r//8 == i//8:
            if board[r] == 0 or IsPlayer(board, r, opponent):
               InsertSort(moves, r)
            else:
               InsertSort(restricted, r)
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
      if InBoard(index) and abs(index//8 - row) == abs(n):
         if board[index] == 0:
            InsertSort(moves, index)
            continue
         elif IsPlayer(board, index, opponent):
            InsertSort(moves, index)
         directions[j] = 0
         InsertSort(restricted, index)
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
      if InBoard(index) and abs(index//8 - row) == abs(n*directions[j][0]):
         if board[index] == 0:
            InsertSort(moves, index)
            continue
         elif IsPlayer(board, index, opponent):
            InsertSort(moves, index)
         directions[j][1] = 0
         InsertSort(restricted, index)
      else:
         directions[j][1] = 0
         #InsertSort(restricted, index)
   return [moves, restricted]

def GetQueenMoves(board, position, player, opponent, row):
   moves = []
   restricted = []
   bish_moves = GetBishopMoves(board, position, player, opponent, row)
   rook_moves = GetRookMoves(board, position, player, opponent, row)
   InsertSort(moves, bish_moves[0])
   InsertSort(restricted, bish_moves[1])
   InsertSort(moves, rook_moves[0])
   InsertSort(restricted, rook_moves[1])
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
         elif InBoard(j):
            if IsPlayer(board, j, player):
               InsertSort(restricted, j)
            else:
               InsertSort(moves, j)
   return [moves, restricted]

##############################
## BRAINS OF THIS OPERATION ##
##############################

class evalTree:

   def __init__(self, board, player, pd, depth, move):
      self.board = board
      self.player = player
      self.pd = pd
      self.depth = depth
      self.move = move
      self.next = []
      self.score = self.genscore()
      self.bcm = [None, None]  # best child move, for minimax
   
   def genscore(self):
      score = 0
      for i in range(0, max(len(self.pd[0]), len(self.pd[1])), 1):
         for j in range(0, 2, 1):
            if i >= len(self.pd[j]):
               continue
            score += PieceValue(self.pd[j][i][0])
            score += PositionValue(self.pd[j][i][0], self.pd[j][i][1])
            score += OptionsRating(self.pd[j][i][0], self.pd[j][i][2])
      #score += RooksConnected(self.pd)
      score += SafetyRating(GenOpponent(self.player), self.pd, self.depth)  # safety of opponenet
      score += RankHeavy(self.player, self.pd)
      score += RankHeavy(GenOpponent(self.player), self.pd)
      return score

   def evalnext(self, q_trav, eT, s_mm):
      p_index = self.player//10 - 1
      opp = GenOpponent(self.player)
      o_index = opp//10 - 1
      #factor = 1
      #if self.player == 10:
      #   factor = -1
      for i in range(0, len(self.pd[p_index]), 1):
         if self.pd[p_index][i][2] == []:
            continue
         for j in self.pd[p_index][i][2]:
            good_take = False
            nB = list(self.board)
            npd = [[], []]
            for n1 in range(0, 2, 1):
               npd[n1] = list(self.pd[n1])
               for n2 in range(0, len(self.pd[n1]), 1):
                  npd[n1][n2] = list(self.pd[n1][n2])
                  npd[n1][n2][2] = list(self.pd[n1][n2][2])
                  npd[n1][n2][3] = list(self.pd[n1][n2][3])
            if IsPlayer(nB, j, opp):
               delete = BinarySearchPDPos(npd[o_index], j)
               #print(npd, delete)
               #a = PieceType(self.pd[o_index][delete][0])
               #if a >= PieceType(self.pd[p_index][i][0]):
               #   good_take = True
               npd[o_index] = npd[o_index][:delete] + npd[o_index][delete + 1:]
               #print(npd)
            nM = [npd[p_index][i][0], npd[p_index][i][1], j]  # new move
            nB[npd[p_index][i][1]] = 0
            nB[j] = npd[p_index][i][0]
            moves_and_restirct = GetPieceLegalMoves(nB, j)
            npd[p_index][i][2] = moves_and_restirct[0]
            npd[p_index][i][3] = moves_and_restirct[1]
            npd[p_index][i][1] = j
            self.UpdatePD(nB, npd, j) 
            self.UpdatePD(nB, npd, self.pd[p_index][i][1])
            BubbleSortPDPos(npd[p_index])
            node = evalTree(nB, opp, npd, self.depth + 1, nM)
            #if (node.score - self.score) > 8888 * factor:
            #   continue
            #if good_take:
            #   node.score += PieceValue(a + GenOpponent(node.player))
            #InsertSortNodes(self.next, node)
            self.next += [node]
      #if self.depth == 2:
      #self.next = self.BestChilds()
      s_mm.push(self)
      for i in self.next:
         q_trav.put(i)
         eT.put(i.bcm)
         s_mm.push(i)
      return True

   def BestChilds(self):  # in the case I want to take a part of the nexts
      a = 1
      if len(self.next) > a:
         if self.player == 10:
            self.next = self.next[len(self.next) - a:len(self.next)]
         else:
            self.next = self.next[0:a]
      if type(self.next) != list:
         return [self.next]
      else:
         return self.next

   def UpdatePD(self, nB, npd, move):  # update an restricted or moves that are altered due to move
      for i in range(0, 2, 1):
         flag = False
         for j in range(0, len(npd[i]), 1):
            index = BinarySearch(npd[i][j][2], move)  # moves list
            if index != -1:
               move_restric = GetPieceLegalMoves(nB, npd[i][j][1])
               npd[i][j][2] = move_restric[0]
               npd[i][j][3] = move_restric[1]
            else:  
               index = BinarySearch(npd[i][j][3], move)  # restricted list
               if index != -1:
                  move_restric = GetPieceLegalMoves(nB, npd[i][j][1])
                  npd[i][j][2] = move_restric[0]
                  npd[i][j][3] = move_restric[1]
      return True

   def minimax(self, s_mm):  # minimax s_mm stack:[a1, b1, b2, b1, c1, c2, b2, c3, c4, c1, d1, d2 ...]
      levelN = []  # level_nodes
      while not s_mm.is_empty():
         node = s_mm.pop()
         levelN += [node]
         if node.bcm == [None, None]:
            node.bcm[0] = node.move
            node.bcm[1] = node.score
         #print(node.bcm)
         if levelN[0].depth != node.depth:  # send the best node to parent
            if node.depth < levelN[0].depth:
               levelN = levelN[0:-1]
               BubbleSortNodes(levelN)  # by bcm[1] score
               self.upBestNode(levelN, node)  # node is parent_node with best bcm
            levelN = [node]
      return True

   def upBestNode(self, levelN, parentN):  #parentN is Parent_Node
      if parentN.player == 10:
         index = -1
      else:
         index = 0
      bestNode = levelN[index]
      if parentN.depth == 0:
         parentN.bcm[0] = bestNode.move 
         parentN.bcm[1] = bestNode.score
      else:
         parentN.bcm[0] = bestNode.move 
         parentN.bcm[1] = bestNode.score
      parentN.score = bestNode.score
      return True

def chessPlayer(board, player):
   status, move, candidiateMoves = True, [], []
   q_trav, eT, s_mm = Queue(), Queue(), Stack()
   root = evalTree(board, player, GenPlayerData(board), 0, [])
   q_trav.put(root)
   eT.put(root.bcm)
   sT = time()  # sT is start_time
   while time() - sT < 8.5:
      node = q_trav.get()
      if node.depth == 2:
         break
      node.evalnext(q_trav, eT, s_mm)  # generate next possibilities
   root.minimax(s_mm)
   #print(root.bcm, "root")
   try:
      if root.bcm[0] == None:
         raise
      move = root.bcm[0][1:]
      big = max(abs(root.next[0].bcm[1]), abs(root.next[-1].bcm[1]))
      #print(big)
      if big == 0.0:
         big = 10
      elif big < 0:
         big *= -1
      for i in root.next:
         candidiateMoves += [[i.move[1:], i.bcm[1]/big]]
   except:
      status = False
      move = False
      candidiateMoves = False
   return [status, move, candidiateMoves, eT.store]

#REMOVE LATER:
#current_board = GenBoard()
#print(chessPlayer(current_board, 10))
#print("---", time() - full, "seconds ---")
