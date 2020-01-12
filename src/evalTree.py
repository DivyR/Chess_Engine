import scoring
import checkers
import sorts
import legal_moves

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
            score += scoring.PieceValue(self.pd[j][i][0])
            score += scoring.PositionValue(self.pd[j][i][0], self.pd[j][i][1])
            score += scoring.OptionsRating(self.pd[j][i][0], self.pd[j][i][2])
      #score += RooksConnected(self.pd)
      score += scoring.SafetyRating(checkers.GenOpponent(self.player), self.pd, self.depth)  # safety of opponenet
      score += scoring.RankHeavy(self.player, self.pd)
      score += scoring.RankHeavy(checkers.GenOpponent(self.player), self.pd)
      return score

   def evalnext(self, q_trav, eT, s_mm):
      p_index = self.player//10 - 1
      opp = checkers.GenOpponent(self.player)
      o_index = opp//10 - 1
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
            if checkers.IsPlayer(nB, j, opp):
               delete = sorts.BinarySearchPDPos(npd[o_index], j)
               #print(npd, delete)
               #a = PieceType(self.pd[o_index][delete][0])
               #if a >= PieceType(self.pd[p_index][i][0]):
               #   good_take = True
               npd[o_index] = npd[o_index][:delete] + npd[o_index][delete + 1:]
               #print(npd)
            nM = [npd[p_index][i][0], npd[p_index][i][1], j]  # new move
            nB[npd[p_index][i][1]] = 0
            nB[j] = npd[p_index][i][0]
            moves_and_restirct =legal_moves.GetPieceLegalMoves(nB, j)
            npd[p_index][i][2] = moves_and_restirct[0]
            npd[p_index][i][3] = moves_and_restirct[1]
            npd[p_index][i][1] = j
            self.UpdatePD(nB, npd, j) 
            self.UpdatePD(nB, npd, self.pd[p_index][i][1])
            sorts.BubbleSortPDPos(npd[p_index])
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
            index = sorts.BinarySearch(npd[i][j][2], move)  # moves list
            if index != -1:
               move_restric = legal_moves.GetPieceLegalMoves(nB, npd[i][j][1])
               npd[i][j][2] = move_restric[0]
               npd[i][j][3] = move_restric[1]
            else:  
               index = sorts.BinarySearch(npd[i][j][3], move)  # restricted list
               if index != -1:
                  move_restric = legal_moves.GetPieceLegalMoves(nB, npd[i][j][1])
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
               sorts.BubbleSortNodes(levelN)  # by bcm[1] score
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