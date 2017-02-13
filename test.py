from suffixtree import SuffixTree


s = "abcabxabcd$"
tree = SuffixTree(s)
tree.build_suffix_tree()
# print("\n".join(tree.print_dfs(tree.root)))

"""
output:

$ [10]
ab [-1]

c [-1]

abxabcd$ [0]
d$ [6]
xabcd$ [3]
b [-1]

c [-1]

abxabcd$ [1]
d$ [7]
xabcd$ [4]
c [-1]

abxabcd$ [2]
d$ [8]
d$ [9]
xabcd$ [5]

"""