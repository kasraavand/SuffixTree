class Base:
    def __init__(self, tree):
        self.tree = tree
        self.main_string = tree._string
        self.root = tree.root


class CheckSubString(Base):
    def __init__(self, tree, sub_string, findall=False):
        super(CheckSubString, self).__init__(tree)
        self.sub_string = sub_string
        self.latest_index = 0
        self.findall = findall
        self.continue_flag = False
        self.sub_length = len(sub_string)

    def traverse(self, node, sub_string):
        if sub_string:
            # Since each child starts with a unique character we will pursue the process for the child that sub-string
            # Starts with the frist character of this edge
            item = next(((char, child) for char, child in node.children.items() if sub_string.startswith(char)), None)

            if item:
                char, child = item
                start, end = child.start, child.end
                # If the edge is equal with sub-string returns the index
                if self.main_string[start: end + 1].startswith(sub_string):
                    if self.findall:
                        return self.find_all_match(child, len(sub_string))
                    return start - (self.sub_length - len(sub_string))
                # sub-string starts with the frist character of our edge but is not equal with it
                # So call the travese for the rest of sub-string (from the lenght of previous edge)
                return self.traverse(child, sub_string[end - start + 1:])
            else:
                # At this level there were no edge that sub-string starts with its leading character.
                return -1
        if self.findall:
            return self.find_all_match(node, len(sub_string))
        return node.start - (self.sub_length - len(sub_string))

    def check(self):
        if self.root is None:
            return -1
        if not isinstance(self.sub_string, str):
            return -1
        if not self.sub_string:
            # Every string starts with an empty string
            return 0

        return self.traverse(self.root, self.sub_string)

    def find_all_match(self, node, sub_length):

        def inner(node, traversed_edges):
            for char, child in node.children.items():
                if child.leaf:
                    yield child.start - traversed_edges
                else:
                    start, end = child.start, child.end
                    sub_length = end - start + 1
                    yield from inner(child, traversed_edges + sub_length)

        if node.leaf:
            first = node.start - (self.sub_length - sub_length)
            return [first, *inner(node, self.sub_length)]
        else:
            return list(inner(node, self.sub_length))
