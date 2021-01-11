from typing import List

import networkx as nx
from itertools import chain, combinations

def find_max_matches(compatible: List[List[bool]]):
    G = build_DiGraph(compatible)
    cycle_list = extract_correct_cycles(G)
    all_cycles_subset = list(powerset(cycle_list))
    max = 0
    temp_set = ()
    for subset in all_cycles_subset:
        s, num = get_num_donates(subset)
        if num > max:
            max = num
            temp_set = s
    print(temp_set)
    for i in range(0, len(temp_set)):
        print("Length",len(temp_set[i]),"cycle: ", end='')
        l = len(temp_set[i])
        if l == 2:
            print(temp_set[i][0], "->", temp_set[i][1], "and", temp_set[i][1], "->", temp_set[i][0], end='')
        else:
            print(temp_set[i][0], "->", temp_set[i][1], "and", temp_set[i][1], "->", temp_set[i][2], "and", temp_set[i][2], "->", temp_set[i][0], end='')
        print()

def build_DiGraph(compatible: List[List[bool]]):
    G = nx.DiGraph()
    rows = len(compatible)
    for i in range(0, rows):
        for j in range(0, len(compatible[i])):
            if compatible[i][j]:
                G.add_edge(i, j)
    return G

def extract_correct_cycles(G: nx.DiGraph):
    cycle_list = []
    for cycle in nx.simple_cycles(G):
        if 2 <= len(cycle) <= 3:
            cycle_list.append(cycle)
    return cycle_list

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def get_num_donates(subset:List[List[int]]):
    n = len(subset)
    temp_set = set([])
    temp_len = 0
    for i in range(0,n):
        num = len(subset[i])
        s = set(subset[i])
        temp_set = temp_set | s
        if len(temp_set) != temp_len + num:
            return (), -1
        temp_len += num
    return subset, temp_len

def example_1():
    a = [[False, False, True, False],
         [True, False, False, False],
         [False, True, False, True],
         [True, True, False, False]]
    find_max_matches(a)

def example_2():
    a = [[False,True,False,True,False,False],
         [False,False,True,True,False,False],
         [True,False,False,False,False,False],
         [False,False,True,False,True,False],
         [False,False,False,True,False,True],
         [False,False,False,False,True,False]]
    find_max_matches(a)

def example_3():
    a = [[False, True, False,False,False,False],
         [True, False,False,False,False,False],
         [False,False,False,True,False,False],
         [False,False,True,False,False,False],
         [False,False,False,False,False,True],
         [False,False,False,False,True,False]]
    find_max_matches(a)

def example_4():
    a = [[False, True, False,True,False],
         [True, False,True,False,True],
         [False,True,False,True,False],
         [True,False,False,False,True],
         [True,False,False,False,False]]
    find_max_matches(a)

def main():
    print("##### example 1 ####")
    example_1()
    print("##### example 2 ####")
    example_2()
    print("##### example 3 ####")
    example_3()
    print("##### example 4 ####")
    example_4()

if __name__ == '__main__':
    main()