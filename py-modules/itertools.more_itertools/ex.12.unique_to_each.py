from more_itertools import unique_to_each

# Graph (adjacency list)
graph = {'A': {'B', 'E'}, 'B': {'A', 'C'},
         'C': {'B'}, 'D': {'E'}, 'E': {'A', 'D'}}

unique_to_each({'B', 'E'}, {'A', 'C'}, {'B'}, {'E'}, {'A', 'D'})
# [[], ['C'], [], [], ['D']]
# If we discard B node, then C gets isolated and if we discard E node, then D gets isolated
