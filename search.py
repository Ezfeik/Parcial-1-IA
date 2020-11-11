from copy import deepcopy
from frog import Frog
from tree import Tree


BOARD = [2, 2, 2, 0, 1, 1, 1]


def heuristic(board):
    """
        Returns a score based in how many values are in the right spot.
    """
    
    score = 0
    for i, j in zip(board, BOARD):
        if i == j:
            score += 1

    return score


def search_solution(tree, eval_heuristic=False):
    """
        Deep-first search python implementation search python implementation with
        Best-first enhancement.

        Parameters
        ----------
        tree: Tree
            Instance with a inicial root node containing the initial state of the game.
        
        eval_heuristic: bool
            If use heuristic.
        
        Returns
        -------
        list[list[int]]
            Board of the Frog game instance.
            
    """

    moves = ['l', 'll', 'r', 'rr']

    count = 0
    history = [tree]
    #state list avoid duplicated values.
    state = [tree.data]
    while history:
        count += 1
        aux_tree = history.pop(0)

        if aux_tree.data.is_solve():
            print("Iterations:", count)
            return aux_tree.chain_to_root()

        #Additional code for auto-expansion of the tree.
        for move in moves:
            new_game = deepcopy(aux_tree.data)
            new_state = new_game.move_to(move)

            if new_state and not new_game in state:
                state.append(new_game)
                tree.add_leaf(new_game, target=aux_tree.data)
        #===============================================

        if eval_heuristic:
            aux_tree.leafs.sort(key=lambda x: heuristic(x.data.get_board()), reverse=True)

        history = aux_tree.leafs + history
    return []
