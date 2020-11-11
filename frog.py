RULES = {
    'l': -1,
    'll': -2,
    'r': 1,
    'rr': 2
}

class Frog:

    def __init__(self, board=[1, 1, 1, 0, 2, 2, 2]):

        self.board = board
        self.pivot = self.board.index(0)


    def get_board(self): return self.board


    def get_pivot(self): return self.pivot


    def _swap(self, move):
        
        p = self.pivot
        m = self.pivot + move

        self.pivot = m

        self.board[p], self.board[m] = self.board[m], self.board[p]

    def move_to(self, move):
        """Move the pivot to a given location.
        
        Parameters
        ----------
        move: str
            Move direction: 'l', 'll', 'r', 'rr'
        
        Returns
        -------
        bool
            Validation of the movement
            
        """
        
        if move in RULES.keys():
            if move.startswith('l'):
                rule = 1
            else:
                rule = 2

            if 0 <= self.pivot + RULES[move] < 7:
                if self.board[self.pivot + RULES[move]] == rule:
                    self._swap(RULES[move])
                    return True

        return False

    def is_solve(self):
        '''
            Return True if board is solve. False otherwise.
        '''
        
        return self.board == [2, 2, 2, 0, 1, 1, 1]


    def __repr__(self):

        return str(self.board)


    def __str__(self):

        return str(self.board)
