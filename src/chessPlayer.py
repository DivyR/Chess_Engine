import sys

sys.path.insert(0, "lib")
from time import time
import boards
import adt
import evalTree
import checkers


def chessPlayer(board, player):
    status, move, candidiateMoves = True, [], []
    q_trav, eT, s_mm = adt.Queue(), adt.Queue(), adt.Stack()
    root = evalTree.evalTree(board, player, checkers.GenPlayerData(board), 0, [])
    q_trav.put(root)
    eT.put(root.bcm)
    sT = time()  # sT is start_time
    while time() - sT < 8.5:
        node = q_trav.get()
        # if node.depth == 2:
        #   break
        node.evalnext(q_trav, eT, s_mm)  # generate next possibilities
    root.minimax(s_mm)
    try:
        if root.bcm[0] == None:
            raise
        move = root.bcm[0][1:]
        big = max(abs(root.next[0].bcm[1]), abs(root.next[-1].bcm[1]))
        # print(big)
        if big == 0.0:
            big = 10
        elif big < 0:
            big *= -1
        for i in root.next:
            candidiateMoves += [[i.move[1:], i.bcm[1] / big]]
    except:
        status = False
        move = False
        candidiateMoves = False
    return [status, move, candidiateMoves, eT.store]
