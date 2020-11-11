from search import *


# Create game instance
game = Frog()

print("Game board initial state:")
print(game)
print('='*24)

# Start the tree of states
init_state = deepcopy(game)
game_tree = Tree(init_state)

solution = search_solution(game_tree, eval_heuristic=False)
solution.reverse()

for move in solution:
    print(move)
print('='*24)

# Final tree
print("Tree print:")
game_tree.print_tree()
