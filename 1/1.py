from itertools import product, permutations

table = "14 17 25 27 34 35 46 56 67"
graph = "BD DE BF FG BC CE CG EA GA"

table += ' ' + table[::-1]
graph += ' ' + graph[::-1]


for per in permutations('ABCDEFG'):
    new_graph = table
    for i in range(1,8):
        new_graph = new_graph.replace(str(i), per[i-1])
    if set(new_graph.split()) == set(graph.split()):
        print(per)
